import React from "react";
import "./upperHeader.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";

export default class SearchBar extends React.Component {
  
  render() {
    const {handleSearch} = this.props;

    return (
      <div className="main__search__bar__wrapper">
        <input
          className="main__search__bar"
          type="text"
          placeholder="Search For Products & Platforms"
          onChange={(e) => handleSearch(e)}
      
        />
        <FontAwesomeIcon
        className="search__icon"
        icon={faSearch}
        onClick={() => {}}
      />
      </div>
    );
  }
}