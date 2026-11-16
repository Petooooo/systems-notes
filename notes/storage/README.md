# Storage & File Systems

Study VFS, EXT4, F2FS, page cache, block I/O, crash consistency, flash translation layers, NVMe and ZNS.

## Structured reading path

1. [VFS and path lookup](vfs-pathwalk-inode-file.mdx)
2. [Page cache, writeback and fsync](page-cache-writeback-fsync.mdx)
3. [bio, blk-mq and NVMe queues](block-io-blk-mq-nvme.mdx)
4. [fio workload design](fio-workload-design.mdx)
5. [ext4, JBD2 and crash consistency](ext4-jbd2-crash-consistency.mdx)
6. [F2FS, segments and garbage collection](f2fs-log-gc-segments.mdx)
7. [NAND flash, FTL and write amplification](nand-ftl-write-amplification.mdx)
8. [NVMe Zoned Namespaces](nvme-zns-zone-lifecycle.mdx)
9. [Storage mini-lab methodology](storage-mini-lab-method.mdx)

Document hardware, filesystem, workload and measurement conditions. Put executable work in [labs/storage](../../labs/storage/).
