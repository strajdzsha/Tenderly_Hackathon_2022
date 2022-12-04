pragma solidity ^0.8.7;

contract Storage {
    address public owner;
    mapping(uint => string) map;

    constructor() {
        owner = msg.sender;
    }

    function get(uint key) public view returns (string memory) {
        return map[key];
    }

    function set(uint key, string memory value) public {
        //require(msg.sender == owner, "Not an owner!");
        map[key]=value;
    }
}