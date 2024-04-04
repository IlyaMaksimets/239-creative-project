import '../styles/LevelStats.css';

export default function LevelStats({info}) {
    console.log(info)
    if (info.stars !== "-") {
        return <>
            <p className={"levelInfoPart"}>Level {info.level}</p>
            <p className={"levelInfoPart"}>Difficulty: {info.difficulty === 0 ? "beginner" :
                info.difficulty === 1 ? "medium" :
                    info.difficulty === 2 ? "hard" : "insane"
            }</p>
            <p className={"levelInfoPart"}>Stars: {info.stars}</p>
            <p className={"levelInfoPart"}>Time: {info.time}</p>
        </>
    } else {
        return <>
            <p className={"levelInfoPart"}>Level {info.level}</p>
            <p className={"levelInfoPart"}>Difficulty: {info.difficulty === 0 ? "beginner" :
                info.difficulty === 1 ? "medium" :
                    info.difficulty === 2 ? "hard" : "insane"
            }</p>
            <p className={"levelInfoPart"}>Stars: -</p>
            <p className={"levelInfoPart"}>Time: -</p>
        </>
    }
}