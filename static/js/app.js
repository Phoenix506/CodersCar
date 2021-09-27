

let buttons = document.querySelectorAll('.bestbtn');

buttons.forEach(button => {
    button.addEventListener('click', function () {
        buttons.forEach(btn => btn.classList.remove('bestactive'));
        this.classList.add('bestactive')
    })
});

let actives = document.querySelectorAll('.formbtn');
actives.forEach(active => {
    active.addEventListener('click', function () {
        actives.forEach(btn => btn.classList.remove('aktiv'));
        this.classList.add('aktiv')
    })
});

function yeniler() {
    var axtarilan = document.getElementById('axtarilan');
    var yeniler = document.getElementById('yeniler');

    axtarilan.style.display = "none"
    yeniler.style.display = "block"

}


function yeniler() {
    var axtarilan = document.getElementById('axtarilan').style.display = "none";
    var yeniler = document.getElementById('yeniler').style.display = "block";

}

function axtarilan() {
    var axtarilan = document.getElementById('axtarilan').style.display = "block";
    var yeniler = document.getElementById('yeniler').style.display = "none";

}

