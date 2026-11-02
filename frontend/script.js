const sessionsBox = document.getElementById("sessions");
const messagesBox = document.getElementById("messages");
const form = document.getElementById("chatForm");
const input = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");

let sessionId = localStorage.getItem("activeSession");
let busy = false;
let viewVersion = 0;

function showMessage(role, content) {
    const welcome = messagesBox.querySelector(".welcome");
    if (welcome) welcome.remove();

    const bubble = document.createElement("div");
    bubble.className = `message ${role}`;
    bubble.textContent = content;

    messagesBox.appendChild(bubble);
    messagesBox.scrollTop = messagesBox.scrollHeight;
    return bubble;
}

async function loadSessions() {
    const response = await fetch("/sessions");
    if (!response.ok) {
        throw new Error("Could not load saved sessions");
    }

    const data = await response.json();
    sessionsBox.replaceChildren();

    for (const id of data.sessions) {
        const button = document.createElement("button");
        button.className = "session";
        button.textContent = id;

        if (id === sessionId) {
            button.classList.add("active");
        }

        button.onclick = () => openSession(id);
        sessionsBox.appendChild(button);
    }
}

async function openSession(id) {
    if (busy) return;

    sessionId = id;
    localStorage.setItem("activeSession", id);
    messagesBox.replaceChildren();

    const version = ++viewVersion;

    try {
        const response = await fetch(
            `/sessions/${encodeURIComponent(id)}/messages`
        );

        if (!response.ok) {
            throw new Error("Could not load conversation");
        }

        const data = await response.json();
        if (version !== viewVersion) return;

        for (const message of data.messages) {
            if (message.role === "human" || message.role === "ai") {
                showMessage(message.role, message.content);
            }
        }

        await loadSessions();

    } catch (error) {
        showMessage("ai", "Error: " + error.message);
    }
}

document.getElementById("newChat").onclick = () => {
    if (busy) return;

    sessionId = crypto.randomUUID();
    localStorage.setItem("activeSession", sessionId);
    ++viewVersion;

    messagesBox.replaceChildren();
    showMessage("ai", "New conversation started. How can I help?");

    loadSessions().catch(console.error);
};

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = input.value.trim();
    if (!message || busy) return;

    if (!sessionId) {
        sessionId = crypto.randomUUID();
        localStorage.setItem("activeSession", sessionId);
    }

    busy = true;
    sendBtn.disabled = true;
    input.value = "";

    showMessage("human", message);
    const loading = showMessage("ai", "Thinking...");

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                session_id: sessionId,
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                typeof data.detail === "string"
                    ? data.detail
                    : "Chat request failed"
            );
        }

        loading.textContent = data.response;
        await loadSessions();

    } catch (error) {
        loading.textContent = "Error: " + error.message;

    } finally {
        busy = false;
        sendBtn.disabled = false;
        input.focus();
    }
});

async function initialize() {
    try {
        await loadSessions();

        if (sessionId) {
            await openSession(sessionId);
        }
    } catch (error) {
        showMessage("ai", "Error: " + error.message);
    }
}

initialize();