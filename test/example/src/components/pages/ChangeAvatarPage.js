import '../styles/ChangeAvatarPage.css';
import url from "../utils";

export default function ChangeAvatarPage({avatar}) {
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status !== 200){
            window.location.replace("http://localhost:3000/")
        }
    });
    
}