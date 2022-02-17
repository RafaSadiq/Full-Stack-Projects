// object.keys
// bitwise operators


// const weights = {
//     green: 1,
//     red: 3,
//     yellow: 2,
// }

// wightedLottery(weights)


const Lottery = weights => {
    let contArray = [];

    Object.keys(weights).forEach(key =>{
        for (let i = 0; i < weights[key]; i++) {
            contArray.push(key);
        }
    })

    return contArray[(Math.random() * contArray.length) | 0];
    
}

const weights = {
    winning: 5,
    losing: 10
}

Lottery(weights)


