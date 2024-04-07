DROP TABLE IF EXISTS ContractData;
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Account;
DROP TABLE IF EXISTS Asset;
DROP TABLE IF EXISTS ModuleHistory;
DROP TYPE IF EXISTS asset_type;
DROP TYPE IF EXISTS transaction_type;
DROP TYPE IF EXISTS option_type;

CREATE TYPE asset_type AS ENUM ('stock', 'option');
CREATE TYPE transaction_type AS ENUM ('buy', 'sell');
CREATE TYPE option_type AS ENUM ('call', 'put');

CREATE TABLE Asset (
  asset_id SERIAL PRIMARY KEY,
  symbol VARCHAR(255) NOT NULL,
  type asset_type NOT NULL
);

CREATE TABLE Account (
  account_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  init_balance DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Transaction (
  t_id SERIAL PRIMARY KEY,
  a_id INT NOT NULL,
  asset_id INT NOT NULL,
  timestamp TIMESTAMP NOT NULL,
  price_per_asset DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL,
  type transaction_type NOT NULL,
  FOREIGN KEY (a_id) REFERENCES Account(account_id),
  FOREIGN KEY (asset_id) REFERENCES Asset(asset_id)
);

CREATE TABLE ContractData (
  c_id SERIAL PRIMARY KEY,
  t_id INT NOT NULL,
  strike DECIMAL(10, 2) NOT NULL,
  expiry TIMESTAMP NOT NULL,
  type option_type NOT NULL
);

CREATE TABLE ModuleHistory (
  m_id SERIAL PRIMARY KEY,
  module_name VARCHAR(255) NOT NULL,
  version VARCHAR(255) NOT NULL,
  timestamp TIMESTAMP NOT NULL
);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO options_trader;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO options_trader;
