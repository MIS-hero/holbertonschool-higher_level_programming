const characterDiv = document.querySelector("#character");

async function fetchCharacter() {
  try {
    const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
    const data = await response.json();
    characterDiv.textContent = data.name;
  } catch (error) {
    console.error("Error fetching character:", error);
  }
}

fetchCharacter();