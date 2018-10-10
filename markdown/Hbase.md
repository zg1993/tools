## 1.Filter
- 比较运算符 CompareOp
   * EQUAL
   * GREATER
   * GREATER_OR_EQUAL
   * LESS
   * LESS_OR_EQUAL
   * NOT_EQUAL
- 比较器 Comparable
 * BinaryComparator
 * BinaryPrefixComparator
 * SubstringComparator


## 2.Rest
### 2.1 JSON
- headers: {'Content-Type': 'application/json', 'Accept': 'application/json'}
- create table

        url: http://localhost:8001/tablename/schema
        data: {
            "ColumnSchema": [
              {"name": 'column1'},
              {'name': 'column2'}]
              }
