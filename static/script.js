// let recognizing = false;
// const micToggle = document.getElementById('micToggle');
// const textInput = document.getElementById('text');
// const messageForm = document.getElementById('messageArea'); // Get the form element

// if (!('webkitSpeechRecognition' in window)) {
//     alert('Your browser does not support speech recognition. Please use Google Chrome.');
// } else {
//     const recognition = new webkitSpeechRecognition();
//     recognition.continuous = true;
//     recognition.interimResults = true;
//     recognition.lang = 'vi-VN'; // Set the language to Vietnamese

//     recognition.onstart = function() {
//         recognizing = true;
//         micToggle.innerHTML = '<i class="fas fa-microphone-slash"></i>'; // Change icon to indicate recording
//     };

//     recognition.onerror = function(event) {
//         console.error(event.error);
//     };

//     recognition.onend = function() {
//         recognizing = false;
//         micToggle.innerHTML = '<i class="fas fa-microphone"></i>'; // Change icon back
//         $(messageForm).submit(); // Use jQuery to trigger the form submission
//     };

//     recognition.onresult = function(event) {
//         let interim_transcript = '';
//         for (let i = event.resultIndex; i < event.results.length; ++i) {
//             if (event.results[i].isFinal) {
//                 // textInput.value += event.results[i][0].transcript;
//                 $(messageForm).submit(); // Use jQuery to trigger the form submission
//             } else {
//                 interim_transcript += event.results[i][0].transcript;
//             }
//         }
//         textInput.value = interim_transcript; // Display the interim results
//     };

//     micToggle.onclick = function() {
//         if (recognizing) {
//             recognition.stop();
//             return;
//         }
//         recognition.start();
//     };
// }

function showPopup(message, seconds) {
    var popup = document.getElementById("popup");
    var overlay = document.querySelector(".overlay");
  
    popup.querySelector("p").textContent = message;
    popup.style.display = "block";
    overlay.style.display = "block"; // Hiển thị lớp phủ mờ
  
    let timer = setInterval(function() {
      seconds--;
      if (seconds == 0) {
        clearInterval(timer);
        popup.style.display = "none";
        overlay.style.display = "none"; // Ẩn lớp phủ khi popup biến mất
      }
    }, 1000);
  }


function kiemTraTuoi(chuoi1, chuoi2) {
    function layNamSinh(chuoi) {
      const kyTuThu4 = chuoi[3];
      const theKy = kyTuThu4 === '0' || kyTuThu4 === '1' ? 19 : 20;
      const namSinh = theKy + chuoi.substring(4, 6);
      return parseInt(namSinh, 10);
    }
  
    // Lấy năm sinh của hai người
    const namSinh1 = layNamSinh(chuoi1);
    const namSinh2 = layNamSinh(chuoi2);
  
    // Kiểm tra độ chênh lệch tuổi
    const chenhLechTuoi = namSinh2 - namSinh1;
    const ketQua = chenhLechTuoi >= 16 ? "hợp lệ" : "không hợp lệ";
    return ketQua
  }
