import { Module } from '@nestjs/common';
import {TerminusModule} from "@nestjs/terminus";
import {HealthController} from "./health.controller";
import { ConfigModule } from '@nestjs/config';
import {BrapiController} from "./brapi/controllers/brapi.controller";


@Module({
  imports: [
      ConfigModule.forRoot({
          isGlobal: true,
      }),
      TerminusModule
  ],
  controllers: [
      HealthController,
      BrapiController
  ],
  providers: [],
})
export class AppModule {}
