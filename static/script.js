let recognizing = false;
const micToggle = document.getElementById('micToggle');
const textInput = document.getElementById('text');
const messageForm = document.getElementById('messageArea'); // Get the form element

if (!('webkitSpeechRecognition' in window)) {
    alert('Your browser does not support speech recognition. Please use Google Chrome.');
} else {
    const recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'vi-VN'; // Set the language to Vietnamese

    recognition.onstart = function() {
        recognizing = true;
        micToggle.innerHTML = '<i class="fas fa-microphone-slash"></i>'; // Change icon to indicate recording
    };

    recognition.onerror = function(event) {
        console.error(event.error);
    };

    recognition.onend = function() {
        recognizing = false;
        micToggle.innerHTML = '<i class="fas fa-microphone"></i>'; // Change icon back
        $(messageForm).submit(); // Use jQuery to trigger the form submission
    };

    recognition.onresult = function(event) {
        let interim_transcript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                // textInput.value += event.results[i][0].transcript;
                $(messageForm).submit(); // Use jQuery to trigger the form submission
            } else {
                interim_transcript += event.results[i][0].transcript;
            }
        }
        textInput.value = interim_transcript; // Display the interim results
    };

    micToggle.onclick = function() {
        if (recognizing) {
            recognition.stop();
            return;
        }
        recognition.start();
    };
}

function showPopup(message) {
    var popup = document.getElementById("popup");
    var overlay = document.querySelector(".overlay");
    var countdown = document.getElementById("countdown");
  
    popup.querySelector("p").textContent = message;
    popup.style.display = "block";
    overlay.style.display = "block"; // Hiển thị lớp phủ mờ
  
    let seconds = 5;
    countdown.textContent = seconds; // Hiển thị đếm ngược ban đầu
  
    let timer = setInterval(function() {
      seconds--;
      countdown.textContent = seconds;
      if (seconds == 0) {
        clearInterval(timer);
        popup.style.display = "none";
        overlay.style.display = "none"; // Ẩn lớp phủ khi popup biến mất
      }
    }, 1000);
  }
// const testInput = document.getElementById("messageArea");
// 		testInput.addEventListener("click", function (){
// 		document.getElementById("videoct").style.top = "-100%";
// 		});
// const khungDN = document.getElementById('process-area');
// const ytVideo = document.getElementById('yt-vid');

// khungDN.addEventListener('mouseover', () => {
//   khungDN.style.opacity = 1; // Fade out on hover
//   khungDN.style.transition = "opacity 0.5s";
//   ytVideo.style.opacity = 0; // Fade out on hover
// });

// khungDN.addEventListener('mouseout', () => {
//     khungDN.style.opacity = 0; // Fade in on mouseout
//     ytVideo.style.opacity = 1;
// });