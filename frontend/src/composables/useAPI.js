export const useAPI = (uid) => {
    const domain = 'http://127.0.0.1:5000/'

    const _fetch = async (path, method, body = null) => {
        if(method === 'GET'){
            return await fetch(domain + 'api/' + path);
        }else{
            if(body == null){
                return await fetch(domain + 'api/' + path, {'method': method});
            }
            return await fetch(domain + 'api/' + path, {'method': method, 'headers': {'Content-Type': 'application/json'}, 'body': JSON.stringify(body)}); 
        }
    }


    const addUser = async () => {
        const res = await _fetch('u', 'POST');
        return (await res.json()).id;
    }
    const deleteUser = async () => {
        _fetch('u/' + uid, 'DELETE');
    }
    const getMyNotes = async () => {
        const res = await _fetch('u/' + uid + '/n', 'GET');
        return (await res.json()).notes;
    }
    const getNote = async (nid) => {
        const res = await _fetch('n/' + nid, 'GET');
        return await res.json();
    }
    const addNote = async () => {
        const res = await _fetch('n', 'POST', {'u': uid});
        return (await res.json()).id;
    }
    const renameNote = async (nid, name) => {
        _fetch('n/' + nid, 'PUT', {'u': uid, 't': name});
    }
    const editNote = async (nid, title, content) => {
        _fetch('n/' + nid, 'PUT', {'u': uid, 't': title, 'c': content});
    }
    const deleteNote = async (nid) => {
        _fetch('n/' + nid, 'DELETE', {'u': uid});
    }
    return { uid, addUser, deleteUser, getMyNotes, getNote, addNote, renameNote, editNote, deleteNote };
}
