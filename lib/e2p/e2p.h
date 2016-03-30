/*
 * e2p.h --- header file for the e2p library
 *
 * %Begin-Header%
 * This file may be redistributed under the terms of the GNU Library
 * General Public License, version 2.
 * %End-Header%
 */

#include <sys/types.h>		/* Needed by dirent.h on netbsd */
#include <stdio.h>
#include <dirent.h>

#include <ext2fs/ext2_fs.h>

#define E2P_FEATURE_COMPAT	0
#define E2P_FEATURE_INCOMPAT	1
#define E2P_FEATURE_RO_INCOMPAT	2
#define E2P_FEATURE_TYPE_MASK	0x03

#define E2P_FEATURE_NEGATE_FLAG	0x80

#define E2P_FS_FEATURE		0
#define E2P_JOURNAL_FEATURE	1

/* `options' for print_flags() */

#define PFOPT_LONG  1 /* Must be 1 for compatibility with `int long_format'. */


__attribute__ ((visibility ("default"))) int fgetflags (const char * name, unsigned long * flags);
__attribute__ ((visibility ("default"))) int fgetversion (const char * name, unsigned long * version);
__attribute__ ((visibility ("default"))) int fsetflags (const char * name, unsigned long flags);
__attribute__ ((visibility ("default"))) int fsetversion (const char * name, unsigned long version);
__attribute__ ((visibility ("default"))) int getflags (int fd, unsigned long * flags);
__attribute__ ((visibility ("default"))) int getversion (int fd, unsigned long * version);
__attribute__ ((visibility ("default"))) int iterate_on_dir (const char * dir_name,
		    int (*func) (const char *, struct dirent *, void *),
		    void * private_arg);
__attribute__ ((visibility ("default"))) void list_super(struct ext2_super_block * s);
__attribute__ ((visibility ("default"))) void list_super2(struct ext2_super_block * s, FILE *f);
__attribute__ ((visibility ("default"))) void print_fs_errors (FILE * f, unsigned short errors);
__attribute__ ((visibility ("default"))) void print_flags (FILE * f, unsigned long flags, unsigned options);
__attribute__ ((visibility ("default"))) void print_fs_state (FILE * f, unsigned short state);
__attribute__ ((visibility ("default"))) int setflags (int fd, unsigned long flags);
__attribute__ ((visibility ("default"))) int setversion (int fd, unsigned long version);

__attribute__ ((visibility ("default"))) const char *e2p_feature2string(int compat, unsigned int mask);
__attribute__ ((visibility ("default"))) const char *e2p_jrnl_feature2string(int compat, unsigned int mask);
__attribute__ ((visibility ("default"))) int e2p_string2feature(char *string, int *compat, unsigned int *mask);
__attribute__ ((visibility ("default"))) int e2p_jrnl_string2feature(char *string, int *compat_type, unsigned int *mask);
__attribute__ ((visibility ("default"))) int e2p_edit_feature(const char *str, __u32 *compat_array, __u32 *ok_array);
__attribute__ ((visibility ("default"))) int e2p_edit_feature2(const char *str, __u32 *compat_array, __u32 *ok_array,
		      __u32 *clear_ok_array, int *type_err,
		      unsigned int *mask_err);

__attribute__ ((visibility ("default"))) int e2p_is_null_uuid(void *uu);
__attribute__ ((visibility ("default"))) void e2p_uuid_to_str(void *uu, char *out);
__attribute__ ((visibility ("default"))) const char *e2p_uuid2str(void *uu);

__attribute__ ((visibility ("default"))) const char *e2p_hash2string(int num);
__attribute__ ((visibility ("default"))) int e2p_string2hash(char *string);

__attribute__ ((visibility ("default"))) const char *e2p_mntopt2string(unsigned int mask);
__attribute__ ((visibility ("default"))) int e2p_string2mntopt(char *string, unsigned int *mask);
__attribute__ ((visibility ("default"))) int e2p_edit_mntopts(const char *str, __u32 *mntopts, __u32 ok);

__attribute__ ((visibility ("default"))) unsigned long parse_num_blocks(const char *arg, int log_block_size);
__attribute__ ((visibility ("default"))) unsigned long long parse_num_blocks2(const char *arg, int log_block_size);

__attribute__ ((visibility ("default"))) char *e2p_os2string(int os_type);
__attribute__ ((visibility ("default"))) int e2p_string2os(char *str);

__attribute__ ((visibility ("default"))) unsigned int e2p_percent(int percent, unsigned int base);
