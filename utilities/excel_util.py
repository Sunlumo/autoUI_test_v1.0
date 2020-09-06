import builtins

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
        sheet = OperateExcel.get_excel(self.excel_path).sheet_by_index(sheet_index)
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

    def read_excel_data(self):
        case_list = []
        step_list = []
        case_step = []
        case_new = []
        all_data = []
        for file_path in self.file_path_list:
            excel_file = ExcelBase(file_path)
            excel = excel_file.get_excel()
            case_row_num = excel.sheet_by_index(0).nrows
            step_row_num = excel.sheet_by_index(1).nrows
            for row in range(1, case_row_num):
                case_list.append(excel.sheet_by_index(0).row_values(row))

            for row in range(1, step_row_num):
                step_list.append(excel.sheet_by_index(1).row_values(row))

            for case in case_list:
                case_id = case[0]
                for step in step_list:
                    if step[1] == case_id:
                        step_data_new = step[:4]
                        for data in step[4:]:
                            if data != '':
                                step_data_new.append(data)
                        for i in range(len(step_data_new), 8):
                            step_data_new.append("")
                        case_step.append(step_data_new)
                case_step_tuple = tuple(case_step)
                case_step.clear()
                case_new.append(case_step_tuple)
            all_data.append(case_new)
        return case_new

    def write_excel_data(self):

        return 0
