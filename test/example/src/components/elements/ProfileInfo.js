import '../styles/ProfileInfo.css';

export default function ProfileInfo({nickname, avatar}) {
    if (avatar === undefined) {
        return <>
            <img className={"avatar"} src={'../images/defaultUserAvatar.jpg'}></img>
            <h1 className={"nickname"}>{nickname}</h1>
        </>
    } else {
        return <>
            <img className={"avatar"}></img>
            <h1 className={"nickname"}>{nickname}</h1>
        </>
    }
}