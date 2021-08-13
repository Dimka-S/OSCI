"""Copyright since 2020, EPAM Systems

   This file is part of OSCI.

   OSCI is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   OSCI is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with OSCI.  If not, see <http://www.gnu.org/licenses/>."""
from typing import Type

from osci.datalake.schemas.public import CompanyCommitsRankingReportSchema
from osci.datalake import DatePeriodType

from .base import Report, GeneralReportFactory


class OSCICommitsRankingFactory(GeneralReportFactory):
    report_base_cls: Type[Report] = type('_Report', (Report,),
                                         dict(base_name='OSCI_commits_ranking',
                                              schema=CompanyCommitsRankingReportSchema))


class OSCICommitsRankingMTD(OSCICommitsRankingFactory.report_base_cls):
    date_period = DatePeriodType.MTD


class OSCICommitsRankingYTD(OSCICommitsRankingFactory.report_base_cls):
    date_period = DatePeriodType.YTD