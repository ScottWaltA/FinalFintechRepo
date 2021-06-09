* 


### Starting the TryTryAgain Network:

​	I. Open up GIT BASH or CMD.EXE

​		a. Create nodes 1&2 with the following code (do not forget to write down the pw you chose!): a. Create a name for your            

​         network. 

​		b.  Type and enter:  ./geth --datadir node1 account new

​		c.  Type and enter:  ./geth --datadir node2 account new

​     	d.  Record the public key from both nodes 1 and 2 ( in notepad, Wordpad, or Word file)       

2. Type and enter ./puppeth.exe  

   a. Chose a network name 

   b. Enter the public keys for node 1 and 2 you recorded earlier

   1. Accounts to seal. 

   2. Accounts to pre-fund

   3. Do not forget the "0x"

   4. Initialize the nodes

      a. Type and enter: ./geth --datadir node1 init {your network name from step #2a}.json

      b. .Type and enter: /geth --datadir node2  init (your network name from step#2a}.json

      

   5. Start the mining: 

      a. Type and run:  ./geth --datadir node1 --unlock "{the public key for node 1 from step #1d}" --mine --rpc --allow-insecure-unlock

      b.  Find inside the node1 mining code: 

      "INFO [06-09|07:50:58.743] Started P2P networking   self=enode://................................@127.0.0.1:30303" 

      c. Copy "enode......@127.0.0.1:30303" (to the end of the quotes)

      c. Type and run:  ./geth --datadir node2 --unlock "{the public key for node 2 from step #1d}" --mine --port 30304 --bootnodes " [paste "enode...."]" --ipcdisable --allow-insecure-unlock

      

