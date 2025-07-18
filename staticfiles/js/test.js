let questions = [];
let answers = [];
let currentPage = 0;
const QUESTIONS_PER_PAGE = 6;

const personalityNames = {
    INTJ: "The Architect",
    INTP: "The Logician",
    ENTJ: "The Commander",
    ENTP: "The Debater",
    INFJ: "The Advocate",
    INFP: "The Mediator",
    ENFJ: "The Protagonist",
    ENFP: "The Campaigner",
    ISTJ: "The Logistician",
    ISFJ: "The Defender",
    ESTJ: "The Executive",
    ESFJ: "The Consul",
    ISTP: "The Virtuoso",
    ISFP: "The Adventurer",
    ESTP: "The Entrepreneur",
    ESFP: "The Entertainer"
};

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
    const mbtiCode = data.mbti.split("-")[0];  // Get only "INTJ"
    const name = personalityNames[mbtiCode] || "Unknown Personality";
    document.getElementById("mbti-name").textContent = name;
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
        Mind: "#4ca3ff",
        Energy: "#f4c542",
        Nature: "#2ecc71",
        Tactics: "#a66dd4",
        Identity: "#e74c3c"
    };

    Object.entries(percentages).forEach(([dimension, traits]) => {
        const [leftTrait, rightTrait] = Object.keys(traits);
        const leftPercent = traits[leftTrait];
        const rightPercent = traits[rightTrait];

        const dominantTrait = leftPercent > rightPercent ? leftTrait : rightTrait;
        const dominantPercent = Math.max(leftPercent, rightPercent);

        const color = traitColors[dimension] || "#4ca3ff";
        const thumbPosition = rightPercent; // since the thumb is aligned from the right

        const container = document.createElement("div");
        container.className = "container";
        container.innerHTML = `
          <div class="header">
            <span class="percentage">${dominantPercent.toFixed(0)}%</span>
            <span>${dominantTrait}</span>
          </div>
          <div class="progress-container">
            <div class="label-left">${leftTrait}</div>
            <div class="bar-wrapper">
              <div class="progress-bar" style="background-color: ${color};">
                <div class="thumb" style="right: ${rightPercent.toFixed(0)}%;"></div>
              </div>
            </div>
            <div class="label-right">${rightTrait}</div>
          </div>
        `;
        traitBarsContainer.appendChild(container);
    });
}

const adminAutoBtn = document.getElementById("admin-auto-fill-btn");
if (adminAutoBtn) {
    adminAutoBtn.addEventListener("click", () => {
        // Fill all questions with "Agree"
        for (let i = 0; i < questions.length; i++) {
            answers[i] = "Disagree";

            // Check the corresponding radio input
            const input = document.querySelector(`input[name="q${i}"][value="Agree"]`);
            if (input) input.checked = true;
        }

        // Re-render to reflect checked buttons if needed
        renderQuestions();

        // Auto-submit
        setTimeout(() => {
            handleSubmit();
        }, 500); // slight delay to ensure UI updates
    });
}
