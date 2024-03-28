import '../styles/Statistics.css';
import LevelStats from "./LevelStats";

export default function Statistics({levelsInfo}) {
    return <>
        <div>
            {levelsInfo.map((levelInfo) => <LevelStats info={levelInfo}/>)}
        </div>
    </>
}