import '../styles/Statistics.css';
import LevelStats from "./LevelStats";

export default function Statistics({levelsInfo}) {
    console.log(levelsInfo)
    return <>
        <div>
            {levelsInfo.map((levelInfo) => <div className={"levelInfo"}><LevelStats info={levelInfo}/></div>)}
        </div>
    </>
}