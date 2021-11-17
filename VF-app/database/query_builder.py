class queryBuilder():
    def __init__(self, database_name, table_name):
        # Database name can be either 'portfolio' or 'watchlist'
        self.database_name = database_name
        # Corrosponds to whatever table you want to modify
        self.table_name = table_name
        # We don't want any of these characters
        self.danger_chars = [';',':',',', '<', '.', '>', '/', '\\', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        # We don't want any of these words
        self.danger_words = ['create', 'drop', 'delete', 'detach', 'alter', 'select', 'update', 'null', 'from', 'where']
        self.table = self.input_sanitisation(self.table_name)

    def input_sanitisation(self, text):
        text = text.lower()
        for c in self.danger_chars:
            if c in text:
                text = text.replace(c, "")
        for word in self.danger_words:
            if word in text:
                text = text.replace(word, '')
        result = text.strip().replace(' ', '_')
        return result

    def create_table(self):
        if self.database_name == 'portfolio':
            output = f"""CREATE TABLE {self.table}
            (ID INT PRIMARY KEY  NOT NULL,
            TICKER TEXT UNIQUE NOT NULL,
            QUANTITY INT NOT NULL,
            BASIS_PRICE REAL NOT NULL);
            """
        elif self.database_name == 'watchlist':
            output = f"""CREATE TABLE {self.table}
            (ID INT PRIMARY KEY  NOT NULL,
            TICKER TEXT UNIQUE NOT NULL,
            PRICE REAL);
            """
        return output

    def insert_into_table(self, insert_num):
        query_values = '?'
        if insert_num != 0 and insert_num != 1:
            query_values += ',?' * (insert_num - 1)
        output = F"INSERT INTO {self.table} VALUES ({query_values})"
        return output

    def select_from_table(self):
        output = F"SELECT * FROM {self.table} WHERE TICKER = ?"
        return output

    def update_into_table(self):
        output = F"UPDATE {self.table} SET QUANTITY = ?, BASIS_PRICE = ? WHERE TICKER = ?"
        return output

    def delete_from_table(self):
        output = F"DELETE FROM {self.table} WHERE TICKER = ?"
        return output

    def drop_table(self):
        output = F"DROP TABLE {self.table}"
        return output

    def total_rows_from_table(self):
        output = F"SELECT COUNT(*) FROM {self.table}"
        return output

    def all_rows_in_table(self):
        output = F"SELECT * FROM {self.table}"
        return output
