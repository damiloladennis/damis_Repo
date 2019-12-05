// function doStuff(data, callback) {
//     callback("done");
// }

// doStuff(true, (result)=>console.log(result));

function doStuff(data){
    return new Promise((resolve, reject)=>{
        let successMessage = {
            status: 'success',
            message: 'All is well!'
        };

        let errorMessage = {
            status: 'error',
            message: 'Oops, there was an error!'
        };

        if(typeof data === 'boolean' && data === true) {
            resolve(successMessage);
        } else {
            reject(errorMessage);
        }
    });
}

doStuff(true).then(
    ()=>{
        let a = false;
        console.log("First doStuff resolved");
        return doStuff(a);
    }
).then(
    ()=>{
        console.log("Second doStuff resolved");
    }
).catch(
    ()=>{
        console.log("An error occured");
    }
);

// doStuff(false).then(
//     (successMessage) => {
//         console.log(successMessage);
//     },
//     (errorMessage)=> {
//         console.log(errorMessage);
//     }
// );