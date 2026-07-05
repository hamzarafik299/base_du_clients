const API_URL = "http://127.0.0.1:8000/contacts/";

// Lire tous les contacts
export async function getContacts() {
    const response = await fetch(API_URL);
    return await response.json();
}

// Lire un seul contact
export async function getContact(id) {
    const response = await fetch(`${API_URL}${id}`);
    return await response.json();
}

// Ajouter un contact
export async function addContact(contact) {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(contact)
    });

    return await response.json();
}

// Supprimer un contact
export async function deleteContact(id) {
    const response = await fetch(`${API_URL}${id}`, {
        method: "DELETE"
    });

    return await response.json();
}

// Modifier un contact
export async function updateContact(id, contact) {
    const response = await fetch(`${API_URL}${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(contact)
    });

    return await response.json();
}