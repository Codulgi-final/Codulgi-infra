document.addEventListener("DOMContentLoaded", function () {
    let refreshInterval = 5000;  // 초기값 5초
    let refreshIntervalID;
    let isFirstLoad = true;  // 첫 로드 여부를 확인하는 변수

    const composeFilesList = document.getElementById("compose-files");
    if (composeFilesList) {
        new Sortable(composeFilesList, {
            animation: 150
        });
    }

    window.removeFile = function (button) {
        const listItem = button.parentElement.parentElement;
        listItem.remove();
    };

    window.showToast = function (message, isSuccess = true) {
        const toastContainer = document.getElementById('toast-container');
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-bg-${isSuccess ? 'success' : 'danger'} border-0`;
        toast.role = 'alert';
        toast.ariaLive = 'assertive';
        toast.ariaAtomic = 'true';
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;
        toastContainer.appendChild(toast);
        const bsToast = new bootstrap.Toast(toast, {delay: 3000});
        bsToast.show();
        toast.addEventListener('hidden.bs.toast', () => {
            toastContainer.removeChild(toast);
        });
    };

    window.executeFile = async function (file, action) {
        try {
            const response = await fetch(`/services/${file}/${action}`, {method: "POST"});
            const result = await response.json();
            showToast(result.message, true);
        } catch (error) {
            console.error(`Error executing ${file} with action ${action}:`, error);
            showToast(`${file}의 ${action}을 실패하였습니다.`, false);
        }
    };

    window.executeInOrder = async function () {
        const fileElements = document.querySelectorAll("#compose-files li");
        const fileNames = Array.from(fileElements).map(el => el.getAttribute("data-file"));
        try {
            const response = await fetch("/execute-order", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({files: fileNames})
            });
            const result = await response.json();
            showToast(result.message, true);
        } catch (error) {
            console.error("에러 로그:", error);
            showToast("순차 컨테이너 실행에 실패 하였습니다.", false);
        }
    };

    window.stopAndRemoveAllContainers = async function () {
        try {
            const response = await fetch("/stop-all-containers", {method: "POST"});
            const result = await response.json();
            showToast(result.message, true);
        } catch (error) {
            showToast("모든 컨테이너 종료하는 것에 실패하였습니다.", false);
        }
    };

    async function updateMonitoringData() {
        const spinner = document.getElementById("monitoring-spinner");
        const monitoringTable = document.getElementById("monitoring-table");
        const tableBody = document.getElementById("monitoring-table-body");

        if (isFirstLoad) {
            spinner.style.display = "block";
            monitoringTable.style.display = "none";
        }

        try {
            const response = await fetch("/api/containers");
            const containers = await response.json();
            tableBody.innerHTML = '';

            containers.forEach(container => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${container.id}</td>
                    <td>${container.name}</td>
                    <td>${container.status}</td>
                    <td>${container.ports}</td>
                    <td>${container.cpu_percent || "N/A"}</td>
                    <td>${container.memory_usage || "N/A"}</td>
                    <td>${container.memory_limit || "N/A"}</td>
                `;
                tableBody.appendChild(row);
            });

            if (isFirstLoad) {
                spinner.style.display = "none";
                monitoringTable.style.display = "table";
                isFirstLoad = false; // 처음에만 스피너 쓰고 이후에는 스피너 안씀
            }
        } catch (error) {
            console.error("Failed to update monitoring data:", error);
            showToast("모니터링 업데이트 실패", false);
        }
    }

    function updateRefreshInterval() {
        clearInterval(refreshIntervalID);
        refreshIntervalID = setInterval(updateMonitoringData, refreshInterval);
    }

    window.updateRefreshInput = function (value) {
        refreshInterval = value * 1000;
        document.getElementById("refresh-interval-input").value = value;
        updateRefreshInterval();
    };

    window.updateRefreshRange = function (value) {
        refreshInterval = value * 1000;
        document.getElementById("refresh-interval-range").value = value;
        updateRefreshInterval();
    };

    // 페이지 로드 시 데이터 초기화 및 주기적 모니터링
    updateMonitoringData();
    refreshIntervalID = setInterval(updateMonitoringData, refreshInterval);
});
