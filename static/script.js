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

// const testInput = document.getElementById("messageArea");
// 		testInput.addEventListener("click", function (){
// 		document.getElementById("videoct").style.top = "-100%";
// 		});
const videoContainer = document.getElementById('process-area');
const ytVideo = document.getElementById('yt-vid');

videoContainer.addEventListener('mouseover', () => {
  videoContainer.style.opacity = 1; // Fade out on hover
  videoContainer.style.transition = "opacity 0.5s";
  ytVideo.style.opacity = 0; // Fade out on hover
});

videoContainer.addEventListener('mouseout', () => {
    videoContainer.style.opacity = 0; // Fade in on mouseout
    ytVideo.style.opacity = 1;
});