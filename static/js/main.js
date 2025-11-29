// Utility to show toasts
function showToast(message, variant = "success") {
    const container = document.getElementById("toast-container");
    if (!container) return;

    const id = `toast-${Date.now()}`;
    const bgClass =
        variant === "success"
            ? "text-bg-success"
            : variant === "error"
            ? "text-bg-danger"
            : "text-bg-secondary";

    const toastEl = document.createElement("div");
    toastEl.className = `toast align-items-center ${bgClass} border-0`;
    toastEl.id = id;
    toastEl.role = "alert";
    toastEl.ariaLive = "assertive";
    toastEl.ariaAtomic = "true";
    toastEl.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;

    container.appendChild(toastEl);

    const bsToast = new bootstrap.Toast(toastEl, { delay: 4000 });
    bsToast.show();

    toastEl.addEventListener("hidden.bs.toast", () => {
        toastEl.remove();
    });
}

function setGlobalLoader(visible) {
    const loader = document.getElementById("global-loader");
    if (!loader) return;
    if (visible) {
        loader.classList.remove("d-none");
    } else {
        loader.classList.add("d-none");
    }
}

// Attach listeners once DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    const trainBtn = document.getElementById("train-btn");
    const trainBtnSecondary = document.getElementById("train-btn-secondary");
    const predictForm = document.getElementById("predict-form");

    async function runTraining() {
        try {
            setGlobalLoader(true);
            showToast("Training pipeline started…", "info");

            const res = await fetch("/train");
            const text = await res.text();

            if (res.ok) {
                showToast(text || "Training finished successfully!", "success");
            } else {
                showToast("Training failed: " + text, "error");
            }
        } catch (err) {
            console.error(err);
            showToast("Something went wrong while training.", "error");
        } finally {
            setGlobalLoader(false);
        }
    }

    if (trainBtn) {
        trainBtn.addEventListener("click", (e) => {
            e.preventDefault();
            runTraining();
        });
    }
    if (trainBtnSecondary) {
        trainBtnSecondary.addEventListener("click", (e) => {
            e.preventDefault();
            runTraining();
        });
    }

    // Optional: show loader on form submit (since we navigate to another page)
    if (predictForm) {
        predictForm.addEventListener("submit", () => {
            setGlobalLoader(true);
        });
    }
});
