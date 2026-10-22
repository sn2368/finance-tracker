create table transactions(
	id integer primary key,
	description text not null,
	amount real not null check(amount>0),
	category text not null,
	transaction_date text not null);

