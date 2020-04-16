# Open Api

Host: `https://explorer.newtonproject.org`

Url prefix: `/api/v{version_number}`, current version number is `3`.

* Get Transaction By Hash

    * url:  `/transaction`

    * request method:  `GET`

    * params:

        |Field | Type | Desc |
        |---|---|---|
        |txid| String | Transaction Hash |
    
    * return:

        |Field | Type | Desc |
        |---|---|---|
        | txid | string | transaction hash |
        | transaction_status | int | transaction status，0-fail 1-success 2-pending |
        | confirmations | string | confirm number |
        | blockheight | int | block height |
        | transaction_index | int | index of transaction |
        | time | int | transaction time |
        | nonce | int | transaction nonce |
        | from_addr | string | New address |
        | from_address | string | hex address |
        | from_contract | boolean | whether contract address |
        | to_addr | string | New address |
        | to_address | string | hex address |
        | to_contract | boolean | whether contract address |
        | value | string | transaction value |
        | fees | string | transaction fee |
        | data | string | input data |
        

* Get Transactions By Address

    * url:  `/transactions`

    * request method:  `GET`

    * params:

        |Field | Type | Desc |
        |---|---|---|
        | limit | int | Page limit |
        | address | String | Wallet Address |
        | pageNum | int | query page number |
        | category | String | `send` is filter by send transactions, `receive` is filter by receive transactions, default is `all` |

    * return
    
        | field | type | description |
        | --- | --- | --- |
        | page | int | page id |
        | pages | int | total page |
        | limit | int | data number per page |
        | total | int | total transaction number |
        | docs | json | transaction list |
        
        * trans:
        
        | field | type | description |
        | --- | --- | --- |
        
        | txid | string | transaction hash |
        | transaction_status | int | transaction status，0-fail 1-success 2-pending |
        | confirmations | string | confirm number |
        | blockheight | int | block height |
        | transaction_index | int | index of transaction |
        | time | int | transaction time |
        | nonce | int | transaction nonce |
        | from_addr | string | New address |
        | from_address | string | hex address |
        | from_contract | boolean | whether contract address |
        | to_addr | string | New address |
        | to_address | string | hex address |
        | to_contract | boolean | whether contract address |
        | value | string | transaction value |
        | fees | string | transaction fee |
        | data | string | input data |

* Get block list

    * url: `blocks`
    
    * request method: `GET`
    
    * params:

        |Field | Type | Desc |
        |---|---|---|
        | blockDate | string | query date |
        | timezone | string | timezone of web client |
        | limit | int | data number per page |
        | pageNum | int | query page id |
    
    * return:

        |Field | Type | Desc |
        |---|---|---|
        | current_page | int | current page id |
        | limit | int | data number per page |
        | total_page | int | total page number |
        | total_blocks | int | total block number |
        | start_block | int | start height of this page |
        | end_block | int | end height of this page |
        | blocks | json | block list |
    
        * block
        
        | field | type | description |
        |---|---|---|
        | height | int | block height |
        | time | int | block timestamp, uint second |
        | txlength | int | transactions number of this block |
        | hash | string | block hash |
        | size | int | block size |
        | nonce | string | nonce of block |
        | validator_url | string | validator url of block, default "" |
        | previousblockhash | string | parent block hash |
        | validator_name | string | validator name of block, default "" |
        | tx | string | default "" |
        | validator | string | default "" |
        | version | string | default 0 |
        | _id | string | block hash |
    
* Get block detail
    
    * url: `/block/:blockhash`
    
    * request method: `GET`
    
    * params:
    
    None
    
    * return:
    
        | field | type | description |
        | --- | --- | --- |
        | height | int | block height |
        | time | int | block time |
        | txlength | int | transaction number |
        | hash | string | block hash |
        | previousblockhash | string | previous block hash |
        | next_blockhash | string | next block hash |
        | size | int | block size |
        | confirmations | int | confirm number |
        | validator_url | string | |
        | validator_name | string | |
        | tx | string | |
        | validator | string | |
        | version | string | |
        | _id | string | |
        | difficulty | int | |
        | total_difficulty | int | |
        | gas_used | int | |
        | gas_percent | float | gas_used / gas_limit * 100 |
        | gas_limit | int | |
        | extra_data | string | |
        | extra_data_utf8 | string | extra_data utf8 |
        | sha3_uncles | string | |
        | nonce | string | |
        | isMainChain | booleand | |
        | current_net | string | |
    
* Get transaction list by date

    * url: `txs/all`
    
    * method: `GET`
    
    * params:
    
        | field | type | required | description |
        | --- | --- | --- | --- |
        | pageNum | int | false | query page id |
        | limit | int | false | data number per page |
        | transDate | string | false | query date |
        | startTimestamp | string | false | start timestamp |
        | timezone | string | false | local timezone |
    
    * return
    
        | field | type | description |
        | --- | --- | --- |
        | current_page | int | page id |
        | total_page | int | total page |
        | limit | int | data number per page |
        | total_transactions | int | total transaction number |
        | trans | json | transaction list |
        
        * trans:
        
        | field | type | description |
        | --- | --- | --- |
        | txid | string | transaction hash |
        | time | int | transaction time |
        | value | int | transaction value |
        | blockhash | string | block hash |
        | blockheight | string | block height |

* Get transaction list by address, block hash or transaction type
    
    * url: `txs`
    
    * method: `GET`
    
    * params:

        | field | type | description | required |
        | --- | --- | --- | --- |
        | pageNum | int | false | page id |
        | limit | int | false | data number per page |
        | type | string | false | transaction type |
        | block | string | false | query block hash |
        | addr | string | false | query address |
        | contract | string | false | quer contract address |
    
    * return
    
        | field | type | description |
        | --- | --- | --- |
        | current_page | int | page id |
        | total_page | int | total page |
        | limit | int | data per page |
        | total_transactions | int | total transaction number |
        | txs | json | transaction list |
        
        * txs
        
        | field | type | description |
        | --- | --- | --- |
        | txid | string | transaction hash |
        | time | int | transaction time |
        | value | int | transaction value |
        | blockhash | string | block hash |
        | blockheight | string | block height |
        
* Get transaction detail

    * url: `/tx/:txid`
    
    * method: `GET`
    
    * params:
        
        None
     
    * return:
    
        | field | type | description |
        | --- | --- | --- |
        | txid | string | transaction hash |
        | transaction_status | int | transaction status，0-fail 1-success 2-pending |
        | confirmations | string | confirm number |
        | blockheight | int | block height |
        | transaction_index | int | index of transaction |
        | time | int | transaction time |
        | nonce | int | transaction nonce |
        | from_addr | string | New address |
        | from_address | string | hex address |
        | from_contract | boolean | whether contract address |
        | to_addr | string | New address |
        | to_address | string | hex address |
        | to_contract | boolean | whether contract address |
        | value | string | transaction value |
        | fees | string | transaction fee |
        | data | string | input data |
        | input_data_utf8 | string | input data decode as utf8 |
        | [input_data_decode](#input_data_decode) | string or json | input data decode |
        | is_internal | boolean | whether internal transaction |
        | total_internal_trans | int | internal transaction number |
        | [internal_info](#internal_info) | json | internal transaction list |
        
        * internal_info <a name="internal_info"></a>
        
            | field | type | description |
            | --- | --- | --- |
            | contract_address | string | from address in NEW format |
            | from_contract | boolean | whether from_address contract address |
            | to_address | string | NEW address |
            | to_contract | boolean | whether to_address contract address |
            | value | string | transaction value |
            | txid | string | transaction id |
            | time | int | transaction time |
        
        * input_data_decode：<a name="input_data_decode"></a>
        
            | field | type | description |
            | --- | --- | --- |
            | function_name | string | function name |
            | function_inputs | list<list> | [[name，type], [name，type]... ] |
            | function_id | string | function hash |
            | decode_input_data | list | params |

* Get address list
    
    * url: `accounts`
    
    * method: `GET`
    
    * params:
        
        | field | type | required | description |
        | --- | --- | --- | --- |
        | pageNum | int | false | query page id |
        | limit | int | false | data per page |
    
    * return
        
        | field | type | description |
        | --- | --- | --- |
        | total_addresses | int | total address number |
        | total_transactions | string | total transaction number |
        | total_page | int | total page |
        | current_page | int | page id |
        | account_list | json | address list |
        
        * account_list
        
            | field | type | description |
            | --- | --- | --- |
            | address | string | address |
            | is_contract | boolean | whether contract address |
            | balance | string | balance |
            | rank | int | rank |
            | txn_count | string | transaction number |

* Get node list
    
    * url: `nodes`
    
    * method: `GET`
    
    * params:
        
        | field | type | required | description |
        | --- | --- | --- | --- |
        | pageNum | int | false | query page id |
        | limit | int | false | data per page |
     
    * return:
        
        | field | type | description |
        | --- | --- | --- |
        | current_page | int | page id |
        | total_page | int | total page |
        | total_nodes_human | int | total number of human nodes |
        | total_locked_amount_human | string | locked amount of human nodes |
        | total_votes_human | string | votes number of human nodes |
        | nodes_data | json | nodes list |
        
        * nodes_data
        
        | field | type | description |
        | --- | --- | --- |
        | rank | int | rank |
        | address | string | node address |
        | node_id | string | node id |
        | node_type | int | node type, 1-promotion 2-business 3-technology |
        | is_partner_node | boolean | whether partner node |
        | locked_amount | string | locked amount |
        | votes | string | votes number |

* Get contract list

    * url: `contracts_list`
    
    * method: `GET`
    
    * params:
        
        | field | type | required | description |
        | --- | --- | --- | --- |
        | pageNum | int | false | query page id |
        | limit | int | false | data per page |
    
    * return:
    
        | field | type | description |
        | --- | --- | --- |
        | total_contracts | int | total contracts number |
        | total_page | int | total page |
        | current_page | int | page id |
        | limit | int | data per page |
        | contract_list | json | contract list |
        
        * contract list:
        
            | field | type | description |
            | --- | --- | --- |
            | contract_address | string | contract address |
            | tx_counts | string | transaction number |
            | time | int | create time |
            | balance | string | balance |

* Get dashboard brief data

    * url: `brief`
    
    * method: `GET`
    
    * params:
        
        None
    
    * return:
        
        | field | type | description |
        | --- | --- | --- |
        | blocks | int | total block number |
        | transactions | int | total transaction number |
        | transaction_increase | int | transaction increase number in past 24 hours |
        | contracts | int | total contracts number |
        | current_tps | int | current block tps |
        | newton_price_cny | string | NEW price in CNY |
        | newton_price_usd | string | NEW price in USD |
        | newton_price_increase | string | newton price increase rate |
        | market_tap_cny | string | market tap in CNY |
        | market_tap_usd | string | market tap in USD |
        | circulating_supply | string | circulating supply amount |
        | total_addresses | int | total address number |
        | address_increase | int | address increase number |
        | newids | int | total newid number |
        | newid_increase | int | newid increase number |
        | human_nodes | int | total human nodes number |
        | locked_amount | string | total locked amount of nodes |
        | incentive_release | string | incentive release amount |
        | new_tax | string | new tax amount |
        | new_tax_increase | string | new tax increase amount |

* Get circulating supply amount

    * url: `supply/circulating`
    
    * method: `GET`
    
    * params:
        
        None
        
    * return:
        
        | field | type | description |
        | --- | --- | --- |
        | circulating_supply | string | circulating supply amount |

* Get max supply amount

    * url: `supply/max`
    
    * method: `GET`
    
    * params:
        
        None
        
    * return:
        
        | field | type | description |
        | --- | --- | --- |
        | max_supply | string | max supply amount |

* Get market price of NEW 

    * url: `market`
    
    * method: `GET`
    
    * params:
        
        None
        
    * return:
        
        "":"0.000398",
        "":"0.002829",
        "":"-2.2222"
        
        | field | type | description |
        | --- | --- | --- |
        | newton_price_usd | string | NEW price in USD |
        | newton_price_cny | string | NEW price in CNY |
        | newton_price_increase | string | NEW price increase rate |