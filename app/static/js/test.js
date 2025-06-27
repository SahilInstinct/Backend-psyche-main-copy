let questions = [];
let answers = [];
let currentPage = 0;
const QUESTIONS_PER_PAGE = 6;

document.addEventListener("DOMContentLoaded", () => {
    fetch("/get-questions/")
        .then(res => res.json())
        .then(data => {
            questions = data.questions;
            answers = Array(questions.length).fill(null);
            renderQuestions();
        });

    document.getElementById("next-btn").addEventListener("click", () => changePage(1));
    document.getElementById("prev-btn").addEventListener("click", () => changePage(-1));
    document.getElementById("submit-btn").addEventListener("click", handleSubmit);
});
function scrollToTestTop() {
  setTimeout(() => {
    window.scrollTo({
      top: document.getElementById("test-container").offsetTop,
      behavior: "smooth"
    });
  }, 50); // delay helps after DOM changes
}

function renderQuestions() {
    const start = currentPage * QUESTIONS_PER_PAGE;
    const end = start + QUESTIONS_PER_PAGE;
    const pageQuestions = questions.slice(start, end);
    const container = document.getElementById("quiz-form");
    container.innerHTML = "";
    const totalPages = Math.ceil(questions.length / QUESTIONS_PER_PAGE);

    // toggle buttons
    if (currentPage === totalPages - 1) {
        document.getElementById("submit-btn").style.display = "inline-block";
        document.getElementById("next-btn").style.display = "none";
    } else {
        document.getElementById("submit-btn").style.display = "none";
        document.getElementById("next-btn").style.display = "inline-block";
    }

    pageQuestions.forEach((q, i) => {
        const qIndex = start + i;
        const block = document.createElement("div");
        block.classList.add("question");

        const questionHTML = `
            <p class="question-text">${q.text}</p>
            <div class="options">
                ${["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
                    .map(option => `
                        <div class="option">
                            <input type="radio" id="q${qIndex}_${option}" name="q${qIndex}" value="${option}" ${answers[qIndex] === option ? "checked" : ""}>
                            <label for="q${qIndex}_${option}">${option}</label>

                        </div>`).join('')}
            </div>`;
        block.innerHTML = questionHTML;
        container.appendChild(block);

        block.querySelectorAll('input[type="radio"]').forEach(input => {
            input.addEventListener("change", () => {
                answers[qIndex] = input.value;
            });
        });
    });

    document.getElementById("progress-indicator").textContent =
        `Page ${currentPage + 1} of ${Math.ceil(questions.length / QUESTIONS_PER_PAGE)}`;

    scrollToTestTop();

}


function changePage(offset) {
    const maxPage = Math.ceil(questions.length / QUESTIONS_PER_PAGE) - 1;
    currentPage = Math.min(Math.max(currentPage + offset, 0), maxPage);
    renderQuestions();
}

function handleSubmit() {
    if (answers.includes(null)) {
        alert("Please answer all questions.");
        return;
    }

    const payload = questions.map((q, index) => ({
        question_id: q.id,
        answer: answers[index]
    }));

    fetch("/submit-answers/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({ responses: payload })
    })

    .then(res => res.json())
    .then(data => {
    if (!isUserAuthenticated) {
    localStorage.setItem("unsaved_mbti", data.mbti);
    localStorage.setItem("unsaved_percentages", JSON.stringify(data.percentages));
}
    document.getElementById("test-container").style.display = "none";
    document.getElementById("result-container").style.display = "block";
    document.getElementById("mbti-result").textContent = `You are: ${data.mbti}`;
    renderTraitBars(data.percentages);
    if (!isUserAuthenticated) {
    localStorage.setItem("unsaved_mbti", data.mbti);
    localStorage.setItem("unsaved_percentages", JSON.stringify(data.percentages));
}

    fetch('/save-result/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({
            mbti: data.mbti,
            percentages: data.percentages
        })
    });
});

}

function getCSRFToken() {
    const name = "csrftoken";
    const cookieValue = document.cookie
        .split("; ")
        .find(row => row.startsWith(name + "="))
        ?.split("=")[1];
    return cookieValue;
}


//result showing

function renderTraitBars(percentages) {
    const traitBarsContainer = document.getElementById("trait-bars");
    traitBarsContainer.innerHTML = "";

    const traitColors = {
        Mind: "#3498db",
        Energy: "#f1c40f",
        Nature: "#2ecc71",
        Tactics: "#8e44ad",
        Identity: "#e74c3c"
    };

    Object.entries(percentages).forEach(([dimension, traits]) => {
        const traitNames = Object.keys(traits);
        const left = traitNames[0];
        const right = traitNames[1];
        const leftPercent = traits[left];
        const rightPercent = traits[right];

        const dominant = leftPercent > rightPercent ? left : right;
        const dominantPercent = Math.max(leftPercent, rightPercent);

        const bar = document.createElement("div");
        bar.className = "trait-bar";
        bar.innerHTML = `
            <div class="trait-header">
                <span>${left}</span>
                <span>${right}</span>
            </div>
            <div class="trait-track" style="--bar-color: ${traitColors[dimension]};">
                <div class="trait-fill" style="width: ${leftPercent}%;"></div>
                <div class="trait-indicator" style="left: ${leftPercent}%;"></div>
            </div>
            <p class="trait-score"><strong>${dominantPercent}% ${dominant}</strong></p>
        `;
        traitBarsContainer.appendChild(bar);
    });
}

