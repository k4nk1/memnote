import { useAPI } from "./useAPI";

export const useUID = async () => {
    const APIs = useAPI('');
    const getUID = () => {
        return localStorage.getItem('uid');
    }
    let uid = getUID();
    if(uid != null && uid.length === 22){
        return uid;
    }else if(uid = await APIs.addUser()){
        localStorage.setItem('uid', uid);
        return uid;
    }
    alert('Could not complete a request for adding UID.');
    return '';
}