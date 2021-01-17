import React, { Component } from "react";
import mapboxgl from 'mapbox-gl';
import {FormGroup, Input, Label} from 'reactstrap'

export default class Map extends Component {
    constructor(props) {
        super(props);
        // this.state = {
        //     viewCompleted: false,
        //     todoList: todoItems
        // };
    }

    componentDidMount() {
        const map = new mapboxgl.Map({
            container: this.mapContainer,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [-74.100803, 40.944631],
            zoom: 20
        });

    }

    render() {
        return (
            <div>
                <div className="header">
                    <h1>Road Safety</h1>
                </div>

                <div>
                    <FormGroup className="input-box">
                        <Label className="one-line-text">Zip Code:</Label>
                        <Input type="email" name="email" id="exampleEmail" placeholder="with a placeholder" />
                    </FormGroup>
                </div>

                <div className="container">
                    <div className="map">
                        <div className="mapContainer" ref={el => this.mapContainer = el} />
                    </div>
                </div>
            </div>
        )
    }

}