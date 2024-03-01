import '../styles/ProfilePage.css';
import ProfileInfo from "../elements/ProfileInfo";
import Statistics from "../elements/Statistics";
import {useState} from "react";
import url from "../utils";

export default function ProfilePage() {
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status !== 200){
            window.location.replace("http://localhost:3000/")
        }
    });

    const emptyLevel = {
        stars: 0,
        hours: 0,
        minutes: 0,
        seconds: 0
    };
    let emptyLevelsInfo = {};
    for(let i = 1; i <= 9; i++){
        emptyLevelsInfo[`${i}`] = emptyLevel
    }
    const [levelsInfo, setLevelsInfo] = useState(emptyLevelsInfo);
    const [nickname, setNickname] = useState("");
    const [avatar, setAvatar] = useState("");
    return <>
        <ProfileInfo nickname = {nickname} avatar = {avatar}/>
        <Statistics levelsInfo = {levelsInfo}/>
    </>
}