import '../styles/LevelStats.css';
import {useState} from "react";

export default function LevelStats({level, info}) {
    const [levelStars, setLevelStars] = useState(info["stars"]);
    const [levelHours, setLevelHours] = useState(info["hours"]);
    const [levelMinutes, setLevelMinutes] = useState(info["minutes"]);
    const [levelSeconds, setLevelSeconds] = useState(info["seconds"]);
    if (levelStars) {
        return <>
            <p className={"levelInfoPart"}>Level {level}</p>
            <p className={"levelInfoPart"}>Stars: {levelStars}</p>
            <p className={"levelInfoPart"}>Time: {levelHours} hours {levelMinutes} minutes {levelSeconds}</p>
        </>
    } else {
        return <>
            <p className={"levelInfoPart"}>Level {level}</p>
            <p className={"levelInfoPart"}>Stars: -</p>
            <p className={"levelInfoPart"}>Time: -</p>
        </>
    }
}