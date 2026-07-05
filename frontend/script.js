import {
  getContacts,
  getContact,
  addContact,
  updateContact,
  deleteContact,
} from "./api.js";

const form = document.getElementById("contact-form");
const nomInput = document.getElementById("nom");
const categorieInput = document.getElementById("categorie");
const telephoneInput = document.getElementById("telephone");
const tableBody = document.getElementById("contact-table");
const serviceInput = document.getElementById("service")
let editingId = null;
async function affiche_contact() {
  const contacts = await getContacts();
  console.log(contacts);
  tableBody.innerHTML = "";
  for (const contact of contacts) {
    tableBody.innerHTML += `
    <tr>
        <td>${contact.nom}</td> 
        <td>${contact.categorie}</td> 
        <td>${contact.telephone}</td> 
        <td>${contact.service}</td> 
        <td> 
        <button class="edit-btn" data-id="${contact.id}"> Modifier </button> 
        <button class="delete-btn" data-id="${contact.id}"> Supprimer </button> 
        </td>
    </tr>
        `;
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const contact = {
    nom: nomInput.value,
    categorie: categorieInput.value,
    telephone: telephoneInput.value,
    service: serviceInput.value
  };
  if (editingId === null) {
    await addContact(contact);
  } else {
    await updateContact(editingId, contact);
    editingId = null;
  }
  form.reset();
  await affiche_contact();
});
tableBody.addEventListener("click", async (event) => {
  if (event.target.classList.contains("delete-btn")) {
    const id = event.target.dataset.id;
    await deleteContact(id);
    await affiche_contact();
    return
  }else if(event.target.classList.contains("edit-btn")){
        editingId = event.target.dataset.id;
        const contact = await getContact(editingId);
        nomInput.value = contact.nom;
        categorieInput.value = contact.categorie;
        telephoneInput.value = contact.telephone;
        serviceInput.value = contact.service;
  }
});

affiche_contact();
