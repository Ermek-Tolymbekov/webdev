import { Component, OnInit, Input } from '@angular/core';
import {Vacancy} from "../models";
import {ActivatedRoute} from "@angular/router";
import {VacancyService} from "../vacancy.service";

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {

  vacancies: Vacancy[] = [];

  constructor(private route: ActivatedRoute,
              private vacancyService: VacancyService) { }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    this.vacancyService.ID = Number(routeParams.get('companyId'));
    this.getVacancies();
  }

  getVacancies(){
    this.vacancyService.getVacancies().subscribe((data) => {
      this.vacancies = data;
    })
  }
}
