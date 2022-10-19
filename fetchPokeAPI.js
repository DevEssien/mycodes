// function response(resp) {
//     if (!resp.ok) {
//         throw new Error('check connection or interruptions');
//     }
//     return resp.json();
// }

fetch('https://pokeapi.co/api/v2/')
.then((res) => {
    if (!res.ok) {
        throw new Error('check connection or interruptions');
    }
    return res.json();
})
.then((data) => {
    const abilityURL= data.ability;
    return fetch(abilityURL);
})
.then((res) => {
    if (!res.ok) {
        throw new Error('check connection or interruptions');
    }
    return res.json();
})
.then((data) => {
    const speedboostURL = data.results[2].url;
    return fetch(speedboostURL);
})
.then((res) => {
    if (!res.ok) {
        throw new Error('check connection or interruptions');
    }
    return res.json(); 
})
.then((data) => {
    console.log(data.effect_entries[1].effect);
})
.catch((err) => {
    console.log('something went wrong', err)
})