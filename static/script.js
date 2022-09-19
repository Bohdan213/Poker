let cards_path = 'static/images/cards/';
let numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
let suits = ['H', 'D', 'S', 'C'];

let getCardPath = (number, suit) => {
    return `${cards_path}${number}${suit}.svg`;
};

let getCardByPath = (path) => {
    return path.slice(path.lastIndexOf('/') + 1).split('.')[0];
}

let latest_request = 0;

document.addEventListener("DOMContentLoaded", () => {
    let probability_table = document.querySelector(".probabilities > table");
    let choose3cards = document.querySelector(".probabilities > p");

    let calculate_probabilities = () => {
        let cards = [];
        for (let card of document.querySelectorAll("img:not(.card_chooser img)")) {
            let name = getCardByPath(card.src);
            if (name !== "BLUE_BACK")
                cards.push(name);
        }
        console.log(cards);
        if (cards.length < 3) {
            probability_table.style.display = 'none';
            choose3cards.style.display = 'block';
        } else {
            probability_table.style.display = 'none';
            choose3cards.style.display = 'block';
            let request_time = Date.now();
            latest_request = Math.max(latest_request, request_time);
            fetch('/probabilities', {
                method: "POST",
                body: JSON.stringify(cards),
                headers: {
                    "Content-Type": "application/json"
                }
            }).then(async response => {
                if (request_time !== latest_request)
                    return;
                if (response.status === 200 && response.statusText === "OK") {
                    let probabilities = await response.json();
                    console.log(probabilities);
                    for (let combination of Object.keys(probabilities))
                        document.getElementById(`probability_${combination}`).innerText = Math.round(probabilities[combination] * 10000) / 100 + "%";
                    probability_table.style.display = 'block';
                    choose3cards.style.display = 'none';
                }
            });
        }
    };

    let selected_card = null;

    let table = document.querySelector(".card_chooser > table");
    for (let number of numbers) {
        let tr = document.createElement('tr');
        for (let suit of suits) {
            let td = document.createElement('td');
            let img = document.createElement('img');
            img.src = getCardPath(number, suit);
            img.onclick = () => {
                selected_card.src = img.src;
                black_box.style.display = 'none';
                card_chooser.style.display = 'none';
                calculate_probabilities();
            }
            td.appendChild(img);
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }

    let deselect_btn = document.getElementById("deselect_btn");
    deselect_btn.onclick = () => {
        for (let card of document.querySelectorAll("img:not(.card_chooser img)")) {
            card.src = `${cards_path}BLUE_BACK.svg`;
        }
        calculate_probabilities();
    }
    deselect_btn.onclick();

    let black_box = document.querySelector(".black_box");
    let card_chooser = document.querySelector(".card_chooser");
    black_box.style.display = 'none';
    card_chooser.style.display = 'none';

    let ui_cards = [...document.querySelectorAll(".table_cards > img"), ...document.querySelectorAll(".player_cards > img")];
    ui_cards.forEach(ui_card => ui_card.onclick = () => {
        selected_card = ui_card;
        black_box.style.display = 'block';
        card_chooser.style.display = 'block';
    });
});