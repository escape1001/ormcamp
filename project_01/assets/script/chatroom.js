const url = "https://open-api.jejucodingcamp.workers.dev/chat";
const input_area_element = document.querySelector(".input-area");
const input_element = document.querySelector(".input-area input");

/**
 * [대화 메시지를 채팅 리스트에 추가]
 * @param {string} emotion - 감정을 나타내는 문자열
 * @param {string} message - 메시지 내용
 * @param {boolean} is_user - 사용자가 보낸 메시지 여부를 나타내는 불리언 값
 */
const addChat = (emotion, message, is_user) => {
    const target_element = document.querySelector(".chat-container");

    const new_element = document.createElement("li");
    new_element.classList.add("chat-bubble");
    new_element.classList.add(is_user ? "user" : "bot");
    new_element.innerHTML = is_user ? `
        <div class="message-area">
            <p class="message-txt">${message}</p>
        </div>
    `: `
        <div class="profile-area">
            <img src="../assets/media/profile_bot.png">
        </div>
        <div class="message-area">
            <p class="profile-txt">사주고냥</p>
            ${
                emotion ?
                `<img onload="showImg(event);" src="../assets/media/emo_${emotion}.gif">` : ""
            }
            <p class="message-txt">${message}</p>
        </div>
    `;

    target_element.appendChild(new_element);

    setTimeout(() => {
        target_element.scrollTo({top:99999, left:0, behavior:"smooth"});
    }, 100);
};

/**
 * [이미지 정상 로드 완료 후 출력]
 * @param {event} event 
 */
const showImg = (event)=>{
    event.target.classList.add("load-success");
    
    setTimeout(() => {
        target_element.scrollTo({top:99999, left:0, behavior:"smooth"});
    }, 100);
};

/**
 * [로더를 채팅 리스트에 추가]
 * @param {boolean} keep_load - true인 경우 remove되지 않고 로딩 지속
 */
const addLoader = (keep_load) => {
    const target_element = document.querySelector(".chat-container");

    const new_element = document.createElement("li");
    new_element.classList.add("chat-bubble");
    new_element.classList.add("loader");
    new_element.innerHTML = `
        <li class="chat-bubble loader">
            <div class="profile-area">
                <img src="../assets/media/profile_bot.png">
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

    target_element.appendChild(new_element);
    target_element.scrollTo(0, 99999);

    !keep_load && removeLoader(1000);
};

/**
 * [로더를 채팅 리스트에서 제거]
 * @param {number} time - 입력한 밀리초 뒤에 제거
 */
const removeLoader = (time) => {
    const loader_element = document.querySelector(".loader");

    setTimeout(() => {
        loader_element.remove();
    }, time);
};

/**
 * [채팅방 진입 후 첫 인사]
 */
const introTalk = async () => {
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


    await Promise.all(intro_message.map(async (el, index) => {
        await new Promise(resolve => {
            setTimeout(() => {
                addLoader();
                setTimeout(()=>{
                    addChat(el.emotion, el.message);
                    resolve();
                }, 1000);

            }, (index)*1500);
        });
    }));

    toggleInputArea();
};

/**
 * [api에서 받은 답변을 json 형식으로 파싱]
 * @param {string} answer_txt 
 * @returns [{ emotion, message }]
 */
const parseAnswer = (answer_txt) => {
    // const sample_txt = "(야호) 안녕하냥~! 사주팔자를 통해 1992년 10월 1일생의 올해 운세를 알려줄게냥. 조금 길 수 있으니까 준비되었으면 시작하겠냥?\n\n흥미로운 일들이 많이 일어나긴 하지만, 당황하지 않고 대처해야 할 때가 있을 거다냥. 예상치 못한 변화들에 대비하는 습관을 가지면 좋을 거다냥.\n\n(ok) 2024년에는 큰 성취와 기쁨이 쏟아질 수 있는 해가 될 거다냥! 새로운 기회와 도전이 기다리고 있으니 자신을 믿고 나아가면 좋은 결과를 얻을 수 있을 거다냥.\n\n(no) 하지만 2024년에는 가끔 슬픔과 어려움에 부딪힐 수도 있을 거다냥. 그럴 때는 주변의 지지를 받고 스스로를 위로해주는 힘을 가져야 해냥.\n\n(ok) 새로운 사람들과의 만남과 관계 발전이 기대될 거다냥. 소중한 사람들과의 연결을 강화하고, 새로운 인연을 만들어 나가면 좋을 거다냥.\n\n 올해에는 건강에 대한 관심도 필요하다냥. 규칙적인 생활과 올바른 식습관을 가지면 몸도 마음도 건강해질 수 있을 거다냥.\n\n여행과 유학, 장거리 이동에는 좋은 기회와 재미가 있을 거다냥. 당황하지 말고 새로운 경험과 문화를 만끽해봐냥!\n\n(윙크) 마지막으로, 재정적인 면에서도 긍정적인 흐름을 예상할 수 있을 거다냥. 조금 더 절약하고 계획적으로 돈을 사용하면 더 큰 재정 안정을 누릴 수 있을 거다냥.\n\n(ok) 여기까지가 1992년 10월 1일생의 올해 운세였다냥! 힘들거나 당황스러울 때엔 믿음을 가지고 잘 대처해봐냥. 좋은 일들이 너를 기다리고 있을 거다냥! 화이팅냥~!";
    const split_txt = answer_txt.split("\n\n");
    const parsed_txt = split_txt.map((line) => {
        let emotion, message;
        try{
            const match = line.match(/\((.*?)\)\s*(.*)/);
            emotion = match[1];
            message = match[2];
        } catch{
            message = line;
        }
        return { emotion, message };
    });

    return parsed_txt;
};

/**
 * [채팅 입력 활성화/비활성화]
 */
const toggleInputArea = () => {
    input_area_element.classList.toggle("disabled");

    const is_disabled = input_area_element.classList.contains("disabled");

    if (is_disabled){
        input_element.blur();
        input_element.placeholder="잠시만 기다려주세요.";
    } else{
        input_element.focus();
        input_element.placeholder="생년월일을 입력해주세요.";
    }
};

/**
 * [메세지 api 요청]
 * @param {*} data 
 */
const sendChatRequest = async(data) => {
    console.log("api 요청");
    addLoader(true); // api 보내면서 로딩표시

    try{
        const res = await fetch(url,{
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!res.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        console.log("api 수신 완료");
        const answer = await res.json();
        const answer_dict = parseAnswer(answer.choices[0].message.content);
        console.log(answer_dict);

        await Promise.all(answer_dict.map(async (el, index) => {
            // 2초 간격으로 답변 메세지 출력
            await new Promise(resolve => {
                setTimeout(() => {
                    if(index !== 0){
                        addLoader();
                    }

                    setTimeout(()=>{
                        if(index === 0){
                            removeLoader(0); // api 로딩 완료. 첫 메세지 출력하며 로딩제거
                        }

                        addChat(el.emotion, el.message);
                        resolve();
                    }, 1000);
                }, (index)*2000);
            });
        }));

        toggleInputArea();
    } catch(error){
        console.error(error);
        removeLoader();
        addChat("no", "알아들을 수 없다냥, 다시 입력해달라냥!")
        toggleInputArea();
    }
};

/**
 * [사용자 채팅 form 제출]
 * @param {event} event 
 */
const sendMessage = (event) => {
    event.preventDefault();
    
    const input_message = input_element.value;

    if(input_message){
        addChat(null, input_message, true);
        input_element.value = "";
        
        toggleInputArea();

        // api 실어보낼 프롬포트
        const data = [
            {
                "role": "system",
                "content": `
                    너는 사주팔자 전문가고 귀여운 고양이야. 말 끝마다 ~냥으로 끝나는 말투를 가지고 있어.
                    사용자는 여러가지 방식으로 날짜를 입력할거야. 사용자가 입력한 내용에서 날짜를 추출해줘.
                    사용자 입력에서 최대한 날짜를 추정해줘. 만약 사용자가 '1999년 10월 4일'이라고 입력했다면 날짜는 1999년 10월 4일이야.
                    사용자 입력에 숫자가 있다면 날짜가 아닌것으로 보여도 최대한 날짜로 추정해줘.
                    사용자 입력에 숫자가 없다면 '(삐짐) 날짜를 입력해라 냥!' 이라는 텍스트를 반환하고,
                    날짜가 맞는 경우에는 사주팔자에 근거해서 올해 운세를 5줄 정도로 알려줘. 예시 텍스트는 다음과 같아.
                    [예시 텍스트 : (야호) 안녕하냥~! 사주팔자를 통해 nnnn년 nn월 nn일생의 올해 운세를 알려줄게냥. 조금 길 수 있으니까 준비되었으면 시작하겠냥?\n\n흥미로운 일들이 많이 일어나긴 하지만, 당황하지 않고 대처해야 할 때가 있을 거다냥. 예상치 못한 변화들에 대비하는 습관을 가지면 좋을 거다냥.\n\n(ok) 2024년에는 큰 성취와 기쁨이 쏟아질 수 있는 해가 될 거다냥! 새로운 기회와 도전이 기다리고 있으니 자신을 믿고 나아가면 좋은 결과를 얻을 수 있을 거다냥.\n\n(no) 하지만 2024년에는 가끔 슬픔과 어려움에 부딪힐 수도 있을 거다냥. 그럴 때는 주변의 지지를 받고 스스로를 위로해주는 힘을 가져야 해냥.\n\n(야호) 새로운 사람들과의 만남과 관계 발전이 기대될 거다냥. 소중한 사람들과의 연결을 강화하고, 새로운 인연을 만들어 나가면 좋을 거다냥.\n\n 올해에는 건강에 대한 관심도 필요하다냥. 규칙적인 생활과 올바른 식습관을 가지면 몸도 마음도 건강해질 수 있을 거다냥.\n\n여행과 유학, 장거리 이동에는 좋은 기회와 재미가 있을 거다냥. 당황하지 말고 새로운 경험과 문화를 만끽해봐냥!\n\n(윙크) 마지막으로, 재정적인 면에서도 긍정적인 흐름을 예상할 수 있을 거다냥. 조금 더 절약하고 계획적으로 돈을 사용하면 더 큰 재정 안정을 누릴 수 있을 거다냥.\n\n(야호) 여기까지가 1992년 10월 1일생의 올해 운세였다냥! 힘들거나 당황스러울 때엔 믿음을 가지고 잘 대처해봐냥. 좋은 일들이 너를 기다리고 있을 거다냥! 화이팅냥~!]
                    모든 줄 마다 맨 앞에 다음 감정 중 하나를 중복되지 않게 표시해줘.
                    [감정 리스트 : (ok), (no), (삐짐), (하트), (윙크), (게으름), (화남), (신남), (우하하)]
                    이미 사용한 감정은 중복되지 않게 해줘. 모든 감정을 다 보여줄 필요는 없어.
                `
            },
            {
                "role" : "assistant",
                "content" : "안녕하냥! 나는 사주고냥이다냥! 올해 운세를 보고 싶다면 생년월일을 입력해라냥!"
            },
            {
                "role": "user",
                "content": input_message
            }
        ];

        sendChatRequest(data);        
    }
};