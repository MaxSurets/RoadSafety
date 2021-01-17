import axios from 'axios'

export function getCoordinates(zip, callback) {
    axios.get('http://localhost:8000/maps/location/?zip=' + zip)
        .then((response) => {
            console.log(response);
            callback(response);
        }, (error) => {
            console.log(error);
        });
}