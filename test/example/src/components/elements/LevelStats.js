import '../styles/LevelStats.css';

export default function LevelStats({info}) {
    console.log(info)
    if (info.stars !== "-") {
        return <>
            <p className={`levelInfoPart${info.difficulty}`}>Level {info.level}</p>
            <p className={`levelInfoPart${info.difficulty}`}>Difficulty: {info.difficulty === 0 ? "beginner" :
                info.difficulty === 1 ? "medium" :
                    info.difficulty === 2 ? "hard" : "insane"
            }</p>
            <p className={`levelInfoPart${info.difficulty}`}>Stars: {info.stars}</p>
            <p className={`levelInfoPart${info.difficulty}`}>Time: {info.time}</p>
        </>
    } else {
        if (info.difficulty !== -1){
            return <>
                <p className={`levelInfoPart${info.difficulty}`}>Level {info.level}</p>
                <p className={`levelInfoPart${info.difficulty}`}>Difficulty: {info.difficulty === 0 ? "beginner" :
                    info.difficulty === 1 ? "medium" :
                        info.difficulty === 2 ? "hard" : "insane"
                }</p>
                <p className={`levelInfoPart${info.difficulty}`}>Stars: -</p>
                <p className={`levelInfoPart${info.difficulty}`}>Time: -</p>
            </>
        }
        else{
            return <>
                <p className={`emInfoPart`}>Endless mode</p>
                <p className={`emInfoPart`}>Distance: {info.distance}</p>
            </>
        }
    }
}