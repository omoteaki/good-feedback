"use strict";


// const audio = document.getElementById("audioPlayer");

// audio.addEventListener("loadedmetadata", function() {
//   var duration = audio.duration;
//   console.log("オーディオの長さ: " + duration + " 秒");
// });

// const list = [
//   {'time': 1.92, 'marker': 'intro'},
//   {'time': 9.6, 'marker': 'A'},
//   {'time': 28.8, 'marker': 'B'},
//   {'time': 44.16, 'marker': "B'"},
//   {'time': 59.52, 'marker': 'C'},
//   {'time': 74.88, 'marker': 'D'},
//   {'time': 90.24, 'marker': "D'"},
//   {'time': 105.6, 'marker': 'inter'},
//   {'time': 120.96, 'marker': '2A'},
//   {'time': 140.16, 'marker': '2B'},
//   {'time': 155.52, 'marker': "2B'"},
//   {'time': 170.88, 'marker': '2C'},
//   {'time': 186.24, 'marker': '2D'},
//   {'time': 201.6, 'marker': "2D'"},
//   // {'time': 218.88, 'marker': 'inter2'},
//   // {'time': 224.64, 'marker': 'E'},
//   // {'time': 240.0, 'marker': "E'"},
//   // {'time': 263.04, 'marker': '3inter'},
//   // {'time': 293.76, 'marker': '4C'},
//   // {'time': 311.04, 'marker': '4D'},
//   // {'time': 324.48, 'marker': "4D'"},
//   // {'time': 339.84, 'marker': '4D"'},
//   // {'time': 357.12, 'marker': '4D"\''},
// ]

// function updateTextDisplay(currentTime) {
//   const textDisplay = document.getElementById("textDisplay");

//   if (currentTime<list[0]["time"]) {
//     console.log("まだマーカーはありません")
//     textDisplay.innerHTML = "まだマーカーはありません";
    
//   } else if (currentTime<list[1]["time"]) {
//     console.log(list[0]["marker"])
//     textDisplay.innerHTML = list[0]["marker"];

//   } else if (currentTime<list[2]["time"]) {
//     console.log(list[1]["marker"])
//     textDisplay.innerHTML = list[1]["marker"];
//   } else {
    
//   }

//   // for (let index = 0; index < list.length; index++) {
//   //   const markerTime = list[index]["time"];
//   //   const marker = list[index]["marker"];
//   //   const nextMarkerTime = list[index + 1]["time"];
//   //   if (currentTime < markerTime) {
//   //     console.log(marker)
//   //     console.log("まだ")
      
//   //     // return
//   //   } else if ( currentTime ) {
//   //     // return
//   //   } else if ( currentTime => markerTime && currentTime < nextMarkerTime) {
//   //     console.log(marker)
//   //     console.log("なう")
//   //     return

//   //   }
//   // }


//   // while (currentTime < 201.5996) {
//   //   let index = 0;
//   //   const markerTime = list[index]["time"];
//   //   if (currentTime < markerTime) {
//   //     console.log(index);
//   //     break;
//   //   } else if (currentTime = markerTime) {
//   //     console.log(index);
//   //     index ++;
//   //     break;
      
//   //   }
//   // }
  
//   // if (currentTime >= markerTime) {
//   //   console.log(list[index]["marker"]);
//   //   textDisplay.innerHTML = list[index]["marker"];
//   //   index ++;
//   // }
//   // for (let index = 0; index < list.length; index++) {
//   //   const markerTime = list[index]["time"];
//   // }

//   // let index = 0
//   // while (currentTime < 210) {
//   //   const markerTime = list[index]["time"];
//   //   if (currentTime >= markerTime) {

//   //     console.log(list[index]["marker"]);
//   //     textDisplay.innerHTML = list[index]["marker"];
//   //     index++;
  
//   //   }
//   // }

//   // currentTimeに基づいてテキストを取得し、表示する処理を実装
//   // 例: テキストは事前に用意された配列やデータベースから取得
//   // その後、textDisplayに表示する
// }

// audio.addEventListener("timeupdate", function() {
//   const currentTime = audio.currentTime;
//   updateTextDisplay(currentTime);
// });






const audio = document.getElementById("audioPlayer");


const list = [
  {'time': 1.92, 'marker': 'intro'},
  {'time': 9.6, 'marker': 'A'},
  {'time': 28.8, 'marker': 'B'},
  {'time': 44.16, 'marker': "B'"},
  {'time': 59.52, 'marker': 'C'},
  {'time': 74.88, 'marker': 'D'},
  {'time': 90.24, 'marker': "D'"},
  {'time': 105.6, 'marker': 'inter'},
  {'time': 120.96, 'marker': '2A'},
  {'time': 140.16, 'marker': '2B'},
  {'time': 155.52, 'marker': "2B'"},
  {'time': 170.88, 'marker': '2C'},
  {'time': 186.24, 'marker': '2D'},
  {'time': 201.6, 'marker': "2D'"},
  // {'time': 218.88, 'marker': 'inter2'},
  // {'time': 224.64, 'marker': 'E'},
  // {'time': 240.0, 'marker': "E'"},
  // {'time': 263.04, 'marker': '3inter'},
  // {'time': 293.76, 'marker': '4C'},
  // {'time': 311.04, 'marker': '4D'},
  // {'time': 324.48, 'marker': "4D'"},
  // {'time': 339.84, 'marker': '4D"'},
  // {'time': 357.12, 'marker': '4D"\''},
]



function updateTextDisplay(currentTime) {
  const textDisplay = document.getElementById("textDisplay");
  
  // リストをイテレート
  for (let i = 0; i < list.length; i++) {
    const markerTime = list[i].time;
    const nextMarkerTime = i < list.length - 1 ? list[i + 1].time : Infinity;

    if (currentTime >= markerTime && currentTime < nextMarkerTime) {
      // currentTimeが現在のマーカーと次のマーカーの間にある場合
      console.log(list[i].marker);
      textDisplay.innerHTML = list[i].marker;
      return; // マッチしたら終了
    }
  }

  // マーカーがない場合
  console.log("まだマーカーはありません");
  textDisplay.innerHTML = "まだマーカーはありません";
}

audio.addEventListener("timeupdate", function() {
  const currentTime = audio.currentTime;
  updateTextDisplay(currentTime);
});



// console.log(textSelect)

function playFromPosition(position) {
  audio.currentTime = position;
  // audio.play();
}

// // テキストがクリックされたときに対応する位置から再生
// const textSelect = document.getElementById("textSelect");

// textSelect.addEventListener("click", function() {
//   console.log(textSelect.value)
//   const position = textSelect.value;
//   playFromPosition(position);
// });

const textList = document.getElementById("textList");

textList.addEventListener("click", function(event) {
  if (event.target.tagName === "LI") {
    const position = event.target.dataset.position;
    playFromPosition(position);
  }
});
