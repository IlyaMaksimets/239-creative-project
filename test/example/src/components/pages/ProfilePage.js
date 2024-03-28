import '../styles/ProfilePage.css';
import ProfileInfo from "../elements/ProfileInfo";
import Statistics from "../elements/Statistics";
import {useState} from "react";
import url from "../utils";

function add_completion(l, info) {
    l[info.difficulty * 9 + info.level - 1] = {
        level: info.level,
        difficulty: info.difficulty,
        stars: info.stars,
        time: info.time
    }
    return l
}

const emptyLevelInfo = [];

for (let i = 0; i < 36; i++) {
    emptyLevelInfo[i] = {
        level: (i + 1) % 9 === 0 ? 9 : (i + 1) % 9,
        difficulty: Math.floor((i) / 9),
        stars: "-",
        time: "-"
    }
}

export default function ProfilePage() {
    const [levelsInfo, setLevelsInfo] = useState(() => emptyLevelInfo);
    const [nickname, setNickname] = useState("");
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status !== 200) {
            window.location.replace("http://localhost:3000/")
        }
    });
    fetch(url("/get_completions"), {
        method: "POST",
        body: JSON.stringify({token: "just_believe_me_this_must_work_so"}),
        headers: {'Content-Type': 'application/json'},
        credentials: "include"
    }).then((response) => response.json()).then((data) => {
        for(let i = 0; i < data.data.length; i++) {
            setLevelsInfo(l => add_completion(l, data.data[i]));
        }
    });
    return <>
        <ProfileInfo nickname={nickname}/>
        <Statistics levelsInfo={levelsInfo}/>
    </>
}