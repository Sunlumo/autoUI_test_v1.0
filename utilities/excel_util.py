import builtins
import copy

import xlrd
import xlwt
import xlutils
import conf.com_config


class ExcelBase(builtins.object):

    def __init__(self, excel_path):
        self.excel_path = excel_path
        self.excel = None

    # 获取excel对象
    def get_excel(self):
        self.excel = xlrd.open_workbook(self.excel_path)
        return self.excel

    # 获取sheet对象
    def get_sheet(self, sheet_index):
        sheet = self.get_excel().sheet_by_index(sheet_index)
        return sheet

    # 获取单元格的对象
    def get_cell_of_object(self, sheet, coordinate=None, row_no=None, cols_no=None):
        # :param sheet: sheet对象
        # :param coordinate: 坐标
        # :param rowNo: 行号
        # :param colsNo: 列号
        # :return: 单元格的对象

        return

    def get_cell_of_value(self, sheet, coordinate=None, row_no=None, cols_no=None):
        # :param sheet: sheet对象
        # :param coordinate: 坐标
        # :param row_no: 行号
        # :param cols_no: 列号
        # :return:cell值
        return

    def get_cols_number(self, sheet):
        # :param sheet: sheet对象
        # :return: sheet中有数据区域的列结束行号
        return

    def get_column(self, sheet, col_no):
        # :param sheet: sheet对象
        # :param col_no: 下标从1开始
        # :return:
        return

    def get_row(self, sheet, row_no):
        # :param sheet: sheet对象
        # :param rowNo: 从1开始
        # :return: 返回的是这一行所有的数据内容组成的tuple
        return

    def get_rows_number(self, sheet):
        # :param sheet: sheet对象
        # :return: sheet中有数据区域的行结束行号
        return

    def get_sheet_by_index(self, sheet_index):
        # :param sheet_index: sheet的索引号
        # :return: sheet对象
        return

    def get_sheet_by_name(self, sheet_name):
        # :param sheet_name: excel中的sheet名字
        # :return: sheet对象
        return

    def get_start_col_number(self, sheet):
        # :param sheet: sheet对象
        # :return: sheet中有数据区域的开始的列号
        return

    def get_start_row_number(self, sheet):
        # :param sheet: sheet对象
        # :return: sheet中有数据区域的开始的行号
        return

    def write_cell(self, sheet, content, coordinate=None, row_no=None, cols_no=None, style=None):
        # :param sheet: sheet对象
        # :param content: 写入的内容
        # :param coordinate: 坐标
        # :param row_no: 行号
        # :param cols_no: 列号
        # :param style: 字体颜色的名字，比如red，green
        # :return:成功返回True
        return

    def write_cell_current_time(self, sheet, coordinate=None, row_no=None, cols_no=None):
        # :param sheet: sheet对象
        # :param coordinate: 坐标
        # :param row_no: 行号，下标从1开始
        # :param cols_no: 列号，下标从1开始
        # :return:成功返回True
        return


class OperateExcel(object):

    def __init__(self, file_path_list):
        self.file_path_list = file_path_list
        self.case_list = []
        self.step_list = []
        self._get_all_cases()
        self._get_all_steps()

    def case_search(self, item):
        # 获取li的开始 结束
        start = 0
        end = len(self.case_list) - 1
        # 只要start和end 还没错开 就一直找
        while start <= end:
            # 通过计算获取当前查找范围的中间位置
            mid = (start + end) // 2
            # 如果中间数就是item则返回True
            if self.case_list[mid][0] == item:
                return self.case_list[mid]
            # 如果mid比item大，说明item可能会出现在mid左边，对左边再查找
            elif self.case_list[mid][0] > item:
                end = mid - 1
            # mid 比item小，说明item有可能在mid右边，对右边再查找
            else:
                start = mid + 1  # 跳出循环说明没找到 返回错误
        return False

    def _get_all_cases(self):
        excel_file = ExcelBase(self.file_path_list[0])
        excel = excel_file.get_excel()
        case_row_num = excel.sheet_by_index(0).nrows
        for row in range(1, case_row_num):
            self.case_list.append(excel.sheet_by_index(0).row_values(row))
        return self.case_list

    def _get_all_steps(self):
        excel_file = ExcelBase(self.file_path_list[0])
        excel = excel_file.get_excel()
        step_row_num = excel.sheet_by_index(1).nrows
        for row in range(1, step_row_num):
            self.step_list.append(excel.sheet_by_index(1).row_values(row))
        return self.step_list

    def read_excel_data(self):
        case_step = []
        case_step_new = []
        all_data = []
        for case in self.case_list:
            case_id = case[0]
            for step in self.step_list:
                if step[1] == case_id:
                    step_data_new = step[:4]
                    for data in step[4:]:
                        if data != '':
                            step_data_new.append(data)
                    for i in range(len(step_data_new), 8):
                        step_data_new.append("")
                    case_step.append(step_data_new)
            case_list_copy = copy.deepcopy(case_step)
            case_step.clear()
            case_step_new.append(case_list_copy)

        lens = len(self.case_list)

        for num in range(0, lens):
            case_list = []
            case_list_copy = copy.deepcopy(self.case_list)
            case_list.append(case_list_copy[num])
            case_list.append(case_step_new[num])
            case_tuple = tuple(case_list)
            all_data.append(case_tuple)

        return all_data

    def get_case_title(self, case_id):

        if case_id == self.case_list[case_id - 1][0]:
            return self.case_list[case_id - 1][3]
        else:
            if self.case_search(case_id) == False:
                return ""
            else:
                return self.case_search(case_id)[3]

    def write_excel_data(self):

        return 0


# oe = OperateExcel(["C:\\Users\\22131\Desktop\\autoUI_test_v1.0\\test_data\\test_baidu.xlsx"])
# oe.read_excel_data()
