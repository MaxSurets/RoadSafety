import React, { Component } from "react";
import mapboxgl from 'mapbox-gl';
import { FormGroup, Input, Label, Button } from 'reactstrap'
import { getCoordinates } from './network'

export default class Map extends Component {
    constructor(props) {
        super(props);
        this.state = {
            long: -23,
            lat: 40.944631,
            zoom: 1,
            zip: ''
        };
        let map;
    }

    componentDidMount() {
        this.map = new mapboxgl.Map({
            container: this.mapContainer,
            style: 'mapbox://styles/msurets/ckk0xo83l1y2g17p44dn4mnm4',
            center: [this.state.lat, this.state.long],
            zoom: 1
        });
    }

    zipChange = (event) => {
        this.setState({ zip: event.target.value })
    }

    changeMap = (result) => {
        let res = result.data
        this.map.setCenter([res.long, res.lat])
        this.map.setZoom(12)
        this.setState({
            lat: -74.100803,
            long: 40.944631,
        })
    }

    submitZip = () => {
        if (this.state.zip.length == 5 && !isNaN(this.state.zip)) {
            getCoordinates(this.state.zip, this.changeMap)
        }
        else {
            alert("Please enter a valid zip code")
        }
    }

    render() {
        return (
            <div style={{ textAlign: "center" }}>

                <div className="col-xs-12 col-md-8">
                    <FormGroup className="input-box">
                        <Label className="one-line-text">Zip Code:</Label>
                        <Input type="text" name="zip" id="zip" placeholder="Ex: 90001, 07410" onChange={this.zipChange} />
                        <Button onClick={this.submitZip}>Submit</Button>
                    </FormGroup>

                    <div className="map">
                        <div className="mapContainer" ref={el => this.mapContainer = el} />
                    </div>
                </div>
            </div>
        )
    }

}