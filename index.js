const myPromise = new Promise((resolve, reject) => {
    let success = true;

    if (success) {
        resolve("ប្រតិបត្តិការជោគជ័យ!");
    } else {
        reject("ប្រតិបត្តិការបរាជ័យ!");
    }
});
myPromise();