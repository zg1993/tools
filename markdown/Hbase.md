# 总览
### 1.hbase 系统架构
- client
 + 通过RPC和HMaster（管理类操作）和HRegionServer(数据读写类操作)通信
- Zookeeper
- HMaster
 + 启用多个HMaster，通过Zookeeper的Master Election机制总有一个Master运行
 + 负责Table和Region的管理工作
    + 管理对用户的增删改查操作
    + 管理HRegionServer的负载均衡，调整Region的分布
    + 在Region Split后，负责新Region的分配
    + 在HRegionServer停机后，负责失效HRegionServer上Region的迁移
- HRegionServer： 相应用户的I/O请求，向HDFS文件系统中读写数据
![](assets/markdown-img-paste-20181011100622511.png)

#### 1.4 HRegionServer
- table & Region
![](assets/markdown-img-paste-20181011161419925.png)
- HRegion对应Table中的Region
- **一个Region用[startkey,endkey]表示，HRegion由多个HStore组成，每个HStore对应table中的一个Column Family存储**
- HStore组成： MemStore和StoreFiles
 + 数据先写入MemStore，满了后flush成一个StoreFile
 + StoreFile数量超过一个阀值后触发Compact操作，StoreFile变大**合并过程触发版本的合并和数据删除，用户的写操作进入内存后立刻返回，保证I/O的高效**，StoreFile大小超过一定阀值后，触发Split，当前的Region分裂成2个Region，有HMaster分配到相应的HRegionServer上。
- flush & compact (cf数量如何影响这两个操作)


![](assets/markdown-img-paste-20181011102240181.png)


### 1.Filter
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
- 比较过滤器 Comparison Filter
 *


### 2.Rest
#### 2.1 JSON
- headers: {'Content-Type': 'application/json', 'Accept': 'application/json'}
- create table

        url: http://localhost:8001/tablename/schema
        data: {
            "ColumnSchema": [
              {"name": 'column1'},
              {'name': 'column2'}]
              }



### document
##### 34 表设计规则
    Aim to have regions sized between 10 and 50 GB.

    Aim to have cells no larger than 10 MB, or 50 MB if you use mob. Otherwise, consider storing your cell data in HDFS and store a pointer to the data in HBase.

    A typical schema has between 1 and 3 column families per table. HBase tables should not be designed to mimic RDBMS tables.

    Around 50-100 regions is a good number for a table with 1 or 2 column families. Remember that a region is a contiguous segment of a column family.

    Keep your column family names as short as possible. The column family names are stored for every value (ignoring prefix encoding). They should not be self-documenting and descriptive like in a typical RDBMS.

    If you are storing time-based machine data or logging information, and the row key is based on device ID or service ID plus time, you can end up with a pattern where older data regions never have additional writes beyond a certain age. In this type of situation, you end up with a small number of active regions and a large number of older regions which have no new writes. For these situations, you can tolerate a larger number of regions because your resource consumption is driven by the active regions only.

    If only one column family is busy with writes, only that column family accomulates memory. Be aware of write patterns when allocating resources.

##### HBASE 4811
[reverse scan](https://issues.apache.org/jira/browse/HBASE-4811)

### Tool
##### YCSB性能测试工具
