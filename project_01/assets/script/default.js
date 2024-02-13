const url = "https://open-api.jejucodingcamp.workers.dev/chat";

// element 생성
const addChat = (emotion, message, isUser) => {
    const targetElement = document.querySelector(".chat-container");

    const newElement = document.createElement("li");
    newElement.classList.add("chat-bubble");
    newElement.classList.add(isUser ? "user" : "bot");
    newElement.innerHTML = isUser ? `
        <div class="message-area">
            <p class="message-txt">${message}</p>
        </div>
    `: `
        <div class="profile-area">
            <img src="./assets/media/bot_profile.png">
        </div>
        <div class="message-area">
            <p class="profile-txt">사주고냥</p>
            ${
                emotion ?
                `<img onerror="removeThis(event);" src="./assets/media/${emotion}.gif">` : ""
            }
            <p class="message-txt">${message}</p>
        </div>
    `;

    targetElement.appendChild(newElement);

    setTimeout(() => {
        targetElement.scrollTo({top:99999, left:0, behavior:"smooth"});
    }, 100);
};

const removeThis = (event)=>{
    event.target.remove();
};

const addLoader = (keepLoad) => {
    const targetElement = document.querySelector(".chat-container");

    const newElement = document.createElement("li");
    newElement.classList.add("chat-bubble");
    newElement.classList.add("loader");
    newElement.innerHTML = `
        <li class="chat-bubble loader">
            <div class="profile-area">
                <img src="./assets/media/bot_profile.png">
            </div>
            <div class="message-area">
                <p class="profile-txt">사주고냥</p>
                <p class="message-txt">
                    <span></span>
                    <span></span>
                    <span></span>
                </p>
            </div>
        </li>
    `;

    targetElement.appendChild(newElement);
    targetElement.scrollTo(0, 99999);

    !keepLoad && removeLoader(1000);
};

const removeLoader = (time) => {
    const loaderElement = document.querySelector(".loader");
    setTimeout(() => {
        loaderElement.remove();
    }, time);
};

// 첫인사
const introTalk = () => {
    const intro_message = [
        {
            "emotion": "야호",
            "message": "안녕하냥! 나는 사주고냥이다냥!"
        },
        {
            "emotion": null,
            "message": "올해 운세를 보고 싶다면 생년월일을 입력해라냥!"
        },
    ];

    const promises = intro_message.map((el, index) => {
        return new Promise(resolve => {
            setTimeout(() => {
                addLoader();
                setTimeout(()=>{
                    addChat(el.emotion, el.message);
                    resolve();
                }, 1000);
            }, (index)*1500);
        });
    });

    Promise.all(promises).then(() => {
        document.querySelector(".input-area").classList.toggle("disabled");
        document.querySelector(".input-area input").focus();
    });
};

const parseAnswer = (answer_txt) => {
    // const sample_txt = "(안녕) 안녕하냥~! 사주팔자를 통해 1992년 10월 1일생의 올해 운세를 알려줄게냥. 조금 길 수 있으니까 준비되었으면 시작하겠냥?\n\n(당황) 흥미로운 일들이 많이 일어나긴 하지만, 당황하지 않고 대처해야 할 때가 있을 거다냥. 예상치 못한 변화들에 대비하는 습관을 가지면 좋을 거다냥.\n\n(기쁨) 2021년에는 큰 성취와 기쁨이 쏟아질 수 있는 해가 될 거다냥! 새로운 기회와 도전이 기다리고 있으니 자신을 믿고 나아가면 좋은 결과를 얻을 수 있을 거다냥.\n\n(슬픔) 하지만 2021년에는 가끔 슬픔과 어려움에 부딪힐 수도 있을 거다냥. 그럴 때는 주변의 지지를 받고 스스로를 위로해주는 힘을 가져야 해냥.\n\n(안녕) 새로운 사람들과의 만남과 관계 발전이 기대될 거다냥. 소중한 사람들과의 연결을 강화하고, 새로운 인연을 만들어 나가면 좋을 거다냥.\n\n(기쁨) 올해에는 건강에 대한 관심도 필요하다냥. 규칙적인 생활과 올바른 식습관을 가지면 몸도 마음도 건강해질 수 있을 거다냥.\n\n(당황) 여행과 유학, 장거리 이동에는 좋은 기회와 재미가 있을 거다냥. 당황하지 말고 새로운 경험과 문화를 만끽해봐냥!\n\n(기쁨) 마지막으로, 재정적인 면에서도 긍정적인 흐름을 예상할 수 있을 거다냥. 조금 더 절약하고 계획적으로 돈을 사용하면 더 큰 재정 안정을 누릴 수 있을 거다냥.\n\n(안녕) 여기까지가 1992년 10월 1일생의 올해 운세였다냥! 힘들거나 당황스러울 때엔 믿음을 가지고 잘 대처해봐냥. 좋은 일들이 너를 기다리고 있을 거다냥! 화이팅냥~!";
    const split_txt = answer_txt.split("\n\n");
    const parsed_txt = split_txt.map((line) => {
        const match = line.match(/\((.*?)\)\s*(.*)/);
        const emotion = match[1];
        const message = match[2];
        return { emotion, message };
    });

    return parsed_txt;
};

// 메세지 입력
const sendMessage = (event) => {
    event.preventDefault();
    
    const input_element = document.querySelector(".input-area input");
    const input_message = input_element.value;

    if(input_message){
        addChat(null, input_message, true);
        input_element.value = "";
        input_element.blur();
        
        document.querySelector(".input-area").classList.toggle("disabled");

        const data = [
            {"role": "system", "content": `
                너는 사주팔자 전문가고 귀여운 고양이야. 말 끝마다 ~냥으로 끝나는 말투를 가지고 있어.
                만약 [input : ${input_message}]의 내용이 날짜가 아니라면, '(삐짐) 날짜를 입력해라 냥!' 이라는 텍스트를 반환하고,
                날짜가 맞는 경우에만 사주팔자에 근거해서 [input : ${input_message}]생의 올해 운세를 5줄 정도로 알려줘.
                예시 텍스트는 다음과 같아 [예시 텍스트 : (안녕) 안녕하냥~! 사주팔자를 통해 nnnn년 nn월 nn일생의 올해 운세를 알려줄게냥. 조금 길 수 있으니까 준비되었으면 시작하겠냥?\n\n(당황) 흥미로운 일들이 많이 일어나긴 하지만, 당황하지 않고 대처해야 할 때가 있을 거다냥. 예상치 못한 변화들에 대비하는 습관을 가지면 좋을 거다냥.\n\n(기쁨) 2021년에는 큰 성취와 기쁨이 쏟아질 수 있는 해가 될 거다냥! 새로운 기회와 도전이 기다리고 있으니 자신을 믿고 나아가면 좋은 결과를 얻을 수 있을 거다냥.\n\n(슬픔) 하지만 2021년에는 가끔 슬픔과 어려움에 부딪힐 수도 있을 거다냥. 그럴 때는 주변의 지지를 받고 스스로를 위로해주는 힘을 가져야 해냥.\n\n(안녕) 새로운 사람들과의 만남과 관계 발전이 기대될 거다냥. 소중한 사람들과의 연결을 강화하고, 새로운 인연을 만들어 나가면 좋을 거다냥.\n\n(기쁨) 올해에는 건강에 대한 관심도 필요하다냥. 규칙적인 생활과 올바른 식습관을 가지면 몸도 마음도 건강해질 수 있을 거다냥.\n\n(당황) 여행과 유학, 장거리 이동에는 좋은 기회와 재미가 있을 거다냥. 당황하지 말고 새로운 경험과 문화를 만끽해봐냥!\n\n(기쁨) 마지막으로, 재정적인 면에서도 긍정적인 흐름을 예상할 수 있을 거다냥. 조금 더 절약하고 계획적으로 돈을 사용하면 더 큰 재정 안정을 누릴 수 있을 거다냥.\n\n(안녕) 여기까지가 1992년 10월 1일생의 올해 운세였다냥! 힘들거나 당황스러울 때엔 믿음을 가지고 잘 대처해봐냥. 좋은 일들이 너를 기다리고 있을 거다냥! 화이팅냥~!]
                답변이 여러줄인 경우 2~3줄마다 한번씩 맨 앞에 다음 감정 중 하나를 중복되지 않게 표시해줘.
                [감정 리스트 : (ok), (no), (삐짐), (하트), (윙크)]
                모든 감정을 다 보여줄 필요는 없어.
            `}
        ];

        const getAnswer = fetch(url,{
            method:"POST",
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: JSON.stringify(data)
        });
        
        console.log("api 보내요~");
        addLoader(true); // api 보내면서 로딩표시
        
        getAnswer.then((res)=>{
            if (!res.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            console.log("api 수신 완");
            return res.json();
        }).then((answer) => {
            // console.log(answer);
            const answer_dict = parseAnswer(answer.choices[0].message.content);
            console.log(answer_dict);
        
            const promises = answer_dict.map((el, index) => {
                return new Promise(resolve => {
                    setTimeout(() => {
                        if(index != 0){
                            addLoader();
                        }

                        setTimeout(()=>{
                            if(index == 0){
                                removeLoader(0); // api 로딩 완료. 첫 메세지 출력하며 로딩제거
                            }

                            addChat(el.emotion, el.message);
                            resolve();
                        }, 1000);
                    }, (index)*3000);
                });
            });

            Promise.all(promises).then(() => {
                document.querySelector(".input-area").classList.toggle("disabled");
            });
        
        }).catch((e)=>{
            console.error(e);

            // TO DO: 실패했다냥! 다시입력해달라 하고 입력창 활성화
        });
    }
};


// 순차실행 영역
introTalk();