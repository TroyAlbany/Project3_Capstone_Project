pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract Top10NFL is ERC721Full {
    constructor() public ERC721Full("Top10NFLtoken", "TOP") {}
    function mintToken(address NFT_Owner, string memory tokenURI, uint256 tokenIDinput) public payable returns (uint256) {
      uint256 tokenID = tokenIDinput;
      _mint(NFT_Owner, tokenID);
      _setTokenURI(tokenID, tokenURI);
      return tokenID;
    }
}
