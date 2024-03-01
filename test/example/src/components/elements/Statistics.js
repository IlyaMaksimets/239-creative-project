import '../styles/Statistics.css';
import LevelStats from "./LevelStats";

export default function Statistics({levelsInfo}) {
    return <>
        <div>
            <LevelStats level={1} info={levelsInfo["1"]}/>
            <LevelStats level={2} info={levelsInfo["2"]}/>
            <LevelStats level={3} info={levelsInfo["3"]}/>
            <LevelStats level={4} info={levelsInfo["4"]}/>
            <LevelStats level={5} info={levelsInfo["5"]}/>
            <LevelStats level={6} info={levelsInfo["6"]}/>
            <LevelStats level={7} info={levelsInfo["7"]}/>
            <LevelStats level={8} info={levelsInfo["8"]}/>
            <LevelStats level={9} info={levelsInfo["9"]}/>
        </div>
    </>
}