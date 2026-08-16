import { Controller, Get, Post, Body, Param } from '@nestjs/common';

@Controller('users')
export class BrapiController {

    @Get()
    findAll(): string {
        return 'Retorna todos os usuários';
    }

    @Get(':id')
    findOne(@Param('id') id: string): string {
        return `Retorna o usuário com ID ${id}`;
    }

    @Post()
    create(@Body() body: any): string {
        return 'Cria um novo usuário';
    }
}